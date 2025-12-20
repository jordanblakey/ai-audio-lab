import asyncio
import logging
from signal import SIGINT, SIGTERM

import grpc
from protos import helloworld_pb2
from protos import helloworld_pb2_grpc


class Greeter(helloworld_pb2_grpc.GreeterServicer):
    async def SayHello(self, request, context):
        return helloworld_pb2.HelloReply(message="Hello, %s" % request.name)


async def serve():
    port = "50051"
    server = grpc.aio.server()
    helloworld_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port("[::]:" + port)
    await server.start()
    print("server started on " + port)

    async def server_graceful_shutdown():
        print("Starting graceful shutdown...")
        await server.stop(5)

    loop = asyncio.get_running_loop()
    for signal in (SIGINT, SIGTERM):
        loop.add_signal_handler(
            signal,
            lambda: asyncio.create_task(server_graceful_shutdown()),
        )

    await server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    asyncio.run(serve())

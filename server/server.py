import asyncio
import logging
from signal import SIGINT, SIGTERM

import grpc
from protos import transcription_pb2
from protos import transcription_pb2_grpc


class WhisperTranscriber(transcription_pb2_grpc.WhisperTranscriberServicer):
    async def StreamTranscription(self, request_iterator, context):
        logging.info("Started new transcription stream")
        async for chunk in request_iterator:
            # For now, just echo back the received audio length
            message = f"Received {len(chunk.data)} bytes of audio"
            logging.info(message)
            yield transcription_pb2.TranscriptionResult(text=message, is_final=False)


async def serve():
    port = "50051"
    server = grpc.aio.server()
    transcription_pb2_grpc.add_WhisperTranscriberServicer_to_server(WhisperTranscriber(), server)
    server.add_insecure_port("[::]:" + port)
    await server.start()
    print(f"Server started on {port}", flush=True)

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
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    asyncio.run(serve())

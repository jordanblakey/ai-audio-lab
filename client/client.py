import logging
import os
import time

import grpc
from protos import helloworld_pb2, helloworld_pb2_grpc


def run():
    target = os.environ.get("SERVER_ADDRESS", "server:50051")
    print(f"Connecting to {target}...")

    # Simple retry logic
    for i in range(5):
        try:
            with grpc.insecure_channel(target) as channel:
                stub = helloworld_pb2_grpc.GreeterStub(channel)
                response = stub.SayHello(
                    helloworld_pb2.HelloRequest(name="tester")
                )
            print("Greeter client received: " + response.message)
            return
        except grpc.RpcError as e:
            print(f"Connection failed: {e}. Retrying in 2s...")
            time.sleep(2)
    print("Failed to connect after 5 attempts.")


if __name__ == "__main__":
    logging.basicConfig()
    run()

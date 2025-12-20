import os
import logging
from typing import Annotated

import grpc
from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from protos import helloworld_pb2, helloworld_pb2_grpc

app = FastAPI()
app.mount("/static", StaticFiles(directory="client/static"), name="static")
templates = Jinja2Templates(directory="client/templates")


# Configure gRPC connection
target = os.environ.get("SERVER_ADDRESS", "server:50051")


async def get_grpc_response(name: str):
    async with grpc.aio.insecure_channel(target) as channel:
        stub = helloworld_pb2_grpc.GreeterStub(channel)
        response = await stub.SayHello(helloworld_pb2.HelloRequest(name=name))
        return response.message


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/send", response_class=HTMLResponse)
async def send_message(request: Request, name: Annotated[str, Form()]):
    try:
        message = await get_grpc_response(name)
    except grpc.RpcError as e:
        message = f"Error: {e}"
    
    return templates.TemplateResponse("index.html", {"request": request, "response": message})


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)

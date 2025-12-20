FROM nvidia/cuda:12.4.1-cudnn-runtime-ubuntu22.04
RUN apt-get update && apt-get install -y python3 python3-pip libcublas-12-4 && \
    ln -sf /usr/bin/python3 /usr/bin/python && \
    ln -sf /usr/bin/pip3 /usr/bin/pip && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app
ENV PYTHONPATH=/app

COPY server/requirements.txt requirements.txt
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install -r requirements.txt

# Copy protos and generate gRPC code first (changes less frequently than server code)
COPY protos/ protos/
RUN python -m grpc_tools.protoc -I . --python_out=. --pyi_out=. --grpc_python_out=. protos/*.proto

# Copy server code last
COPY server/ server/

EXPOSE 50051

CMD ["python", "server/server.py"]

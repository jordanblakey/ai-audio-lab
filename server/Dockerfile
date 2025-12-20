FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

ENV PYTHONPATH=/app

# Copy server code
COPY server/ server/
# Copy protos package (contains both .proto and generated files now)
COPY protos/ protos/

EXPOSE 50051

CMD ["python", "server/server.py"]

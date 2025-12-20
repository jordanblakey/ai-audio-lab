FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

ENV PYTHONPATH=/app

# Copy client code
COPY client/ client/
# Copy protos package (contains both .proto and generated files now)
COPY protos/ protos/

CMD ["python", "client/client.py"]

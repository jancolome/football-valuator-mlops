FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY data/ ./data/
COPY models/ ./models/
COPY tests/ ./tests/
COPY notebooks/ ./notebooks/

CMD ["pytest", "tests/test_modelo.py", "-v"]

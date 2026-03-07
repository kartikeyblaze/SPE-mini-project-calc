FROM python:3.9-slim

WORKDIR /app

COPY Calculator.py .

CMD ["python", "Calculator.py"]

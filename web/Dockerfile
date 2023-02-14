FROM python:3.10.10-slim AS builder

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update
RUN apt-get install -y --no-install-recommends build-essential gcc

RUN python -m venv /app/venv
ENV PATH="/app/venv/bin:$PATH"

COPY requirements.txt .
RUN pip install -r requirements.txt

FROM python:3.10.10-slim

WORKDIR /app/venv

COPY --from=builder /app/venv /app/venv
COPY . .

ENV PATH="/app/venv/bin:$PATH"

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "-w", "3", "run:app"]

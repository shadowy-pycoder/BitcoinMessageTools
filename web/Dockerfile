FROM python:3.10.10-slim AS builder

WORKDIR /app

RUN apt-get update
RUN apt-get install -y --no-install-recommends build-essential gcc

RUN python -m venv /app/venv
ENV PATH="/app/venv/bin:$PATH"

COPY requirements.txt .
RUN pip install -r requirements.txt

FROM python:3.10.10-slim

RUN groupadd -g 999 python && useradd -r -u 999 -g python python

RUN mkdir /app && chown python:python /app
WORKDIR /app

COPY --chown=python:python --from=builder /app/venv ./venv
COPY --chown=python:python . .

USER 999

ENV PATH="/app/venv/bin:$PATH"

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "-w", "3", "run:app"]





FROM python:3.10-slim-bookworm

HEALTHCHECK NONE

RUN useradd leyley
USER leyledy

COPY . /app
WORKDIR /app

USER root

ENV CHROMIUM_VERSION=119.0.6045.159-1~deb12u1

RUN apt-get update && \
    apt-get install --no-install-recommends -y chromium=${CHROMIUM_VERSION} && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    pip3 install --no-cache-dir -r requirements.txt && \
    chown -R leyley:leyley /app

USER leyley

CMD ["python3", "src/main.py"]

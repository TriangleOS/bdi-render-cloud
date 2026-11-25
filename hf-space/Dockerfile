FROM node:22-bookworm-slim
RUN apt-get update && apt-get install -y --no-install-recommends ffmpeg chromium python3 python3-pip curl unzip fonts-noto-color-emoji ca-certificates \
  && rm -rf /var/lib/apt/lists/* && pip3 install --break-system-packages --no-cache-dir kokoro-onnx soundfile
ENV HYPERFRAMES_BROWSER_PATH=/usr/bin/chromium HYPERFRAMES_TELEMETRY=0 DO_NOT_TRACK=1 HOME=/home/user BDI_MACHINE_NAME=hf-space
RUN useradd -m -u 1000 user || true
USER 1000
WORKDIR /home/user
COPY --chown=1000 start.sh .
CMD ["bash", "start.sh"]

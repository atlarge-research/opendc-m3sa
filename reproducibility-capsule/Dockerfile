FROM python:3.12-slim

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        bash \
        build-essential \
        ca-certificates \
        curl \
        git \
        make \
        openjdk-21-jdk-headless \
        unzip \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /opt/m3sa
COPY reproducibility-capsule/bin/m3sa/requirements.txt ./requirements.txt
RUN python -m venv /opt/m3sa/venv \
    && /opt/m3sa/venv/bin/pip install --upgrade pip \
    && /opt/m3sa/venv/bin/pip install -r requirements.txt

ENV VIRTUAL_ENV=/opt/m3sa/venv
ENV PATH="${VIRTUAL_ENV}/bin:${PATH}"

WORKDIR /workspace

ENTRYPOINT ["/bin/bash"]
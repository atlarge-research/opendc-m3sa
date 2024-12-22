FROM python:3.12-slim

RUN echo "deb http://deb.debian.org/debian sid main" > /etc/apt/sources.list.d/sid.list

# Update and install required packages
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    bash \
    build-essential \
    curl \
    gnupg \
    openjdk-21-jdk \
    && rm -rf /var/lib/apt/lists/*

# Set up working directory
WORKDIR /m3sa

# Copy the current working directory into the container
COPY . /m3sa

# Set script permissions
RUN mkdir -p $HOME/.local/bin

RUN chmod +x /m3sa/m3sa-experiment

RUN cd /m3sa/bin/m3sa && make install

# Default command to execute the script
CMD ["/bin/bash", "-c", "./m3sa-experiment"]

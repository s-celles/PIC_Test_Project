# Use base image for the development container
#FROM ubuntu:22.04
FROM mcr.microsoft.com/devcontainers/base:ubuntu-22.04

# Avoid interactive prompts during installation
ENV DEBIAN_FRONTEND=noninteractive

# Update system and install basic dependencies
RUN apt-get update && apt-get install -y \
    wget \
    curl \
    git \
    build-essential \
    python3 \
    python3-pip \
    python3-venv \
    unzip \
    sudo \
    ca-certificates \
    gnupg \
    lsb-release \
    software-properties-common \
    libc6-dev \
    libusb-1.0.0 \
    openjdk-8-jre \
    && rm -rf /var/lib/apt/lists/*

# Create a non-root user
# RUN useradd -m -s /bin/bash vscode && \
#    echo "vscode ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

# Create destination directory for XC8 (will be installed later)
RUN mkdir -p /opt/microchip && \
    chown -R vscode:vscode /opt/microchip

# Note: XC8 will be installed in post-create script to avoid build timeouts

# Switch to vscode user
USER vscode

# Set working directory
WORKDIR /workspaces/xc8-wrapper

# Add XC8 PATH to .bashrc
RUN echo 'export PATH="/opt/microchip/bin:${PATH}"' >> /home/vscode/.bashrc && \
    echo 'export PATH="/home/vscode/.local/bin:${PATH}"' >> /home/vscode/.bashrc

CMD ["/bin/bash"]

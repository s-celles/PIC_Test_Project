# Makefile for PIC development with Docker

.PHONY: help build run gui compile upload clean logs

# Display help
help:
	@echo "🔧 Available commands for PIC development:"
	@echo ""
	@echo "  build     - Build Docker image with XC8 and MPLAB X"
	@echo "  run       - Launch development container"
	@echo "  gui       - Launch container with GUI support"
	@echo "  compile   - Compile PIC project"
	@echo "  upload    - Program microcontroller"
	@echo "  shell     - Open shell in container"
	@echo "  clean     - Clean containers and images"
	@echo "  logs      - Display container logs"
	@echo ""
	@echo "Examples:"
	@echo "  make build    # First time setup"
	@echo "  make gui      # Development with MPLAB X"
	@echo "  make compile  # Quick compilation"

# Build Docker image
build:
	@echo "🔨 Building Docker image..."
	docker-compose build pic-dev

# Launch interactive development container
run:
	@echo "🚀 Launching development container..."
	docker-compose run --rm pic-dev

# Launch container with GUI support
gui:
	@echo "🖥️  Launching with GUI support..."
	@echo "Make sure X11 forwarding is configured:"
	@echo "  Linux: xhost +local:docker"
	@echo "  macOS: Start XQuartz"
	@echo "  Windows: Launch VcXsrv"
	@echo ""
ifneq ($(OS),Windows_NT)
	@if [ -z "$(DISPLAY)" ]; then \
		echo "⚠️  DISPLAY variable not set!"; \
		echo "Try: export DISPLAY=:0"; \
	fi
endif
	docker-compose run --rm pic-dev

# Compile the project
compile:
	@echo "⚙️  Compiling PIC project..."
	docker-compose run --rm pic-build

# Program the microcontroller
upload:
	@echo "📡 Programming microcontroller..."
	docker-compose run --rm --privileged pic-dev python upload.py

# Open shell in container
shell:
	@echo "🐚 Opening shell in container..."
	docker-compose run --rm pic-dev /bin/bash

# Launch MPLAB X IDE
mplab:
	@echo "🔧 Launching MPLAB X IDE..."
	docker-compose run --rm pic-dev bash .devcontainer/launch-mplab.sh

# Clean containers and images
clean:
	@echo "🧹 Cleaning containers and images..."
	docker-compose down -v
	docker system prune -f

# Display logs
logs:
	@echo "📋 Container logs..."
	docker-compose logs pic-dev

# Run all tests
test:
	@echo "🧪 Running tests..."
	docker-compose run --rm pic-dev python -m pytest

# Install dependencies
install:
	@echo "📦 Installing dependencies..."
	docker-compose run --rm pic-dev bash .devcontainer/post-create.sh

# Display container status
status:
	@echo "📊 Container status:"
	docker-compose ps
	@echo ""
	@echo "📊 Docker images:"
	docker images | grep -E "(pic|xc8|mplab)"

# Launch container for VS Code development
vscode:
	@echo "💻 Preparing for VS Code Dev Containers..."
	@echo "Open VS Code and use 'Dev Containers: Reopen in Container'"

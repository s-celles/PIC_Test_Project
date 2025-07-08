# PIC Development Container

This devcontainer provides a complete development environment for PIC microcontrollers with:

- **XC8 Compiler v3.00** : C compiler for PIC microcontrollers
- **xc8-wrapper** and **ipecmd-wrapper** : Modern Python wrappers
- **Development tools** : Python, build tools, VS Code extensions
- **Cross-platform support** : Works on Windows, Linux, and macOS

## 🚀 Quick Start

### 1. Prerequisites

- **Docker Desktop** installed and running
- **VS Code** with "Dev Containers" extension
- **X11 forwarding** configured for GUI support (Linux/macOS)

### 2. Launch the devcontainer

1. Open this project in VS Code
2. Press `Ctrl+Shift+P` (or `Cmd+Shift+P` on macOS)
3. Type "Dev Containers: Reopen in Container"
4. Wait for automatic build and configuration

### 3. First use

Once the container is started, all tools are configured and ready:

```bash
# Check installation
xc8-wrapper --version
ipecmd-wrapper --version

# Compile the project
python compile.py

# Program the microcontroller (with programmer connected)
python upload.py
```

⚠️ **Note**: HEX file upload from dev containers has not been tested yet. For programming, you may need to use the host system or copy files outside the container.

## 🛠️ Available Tools

### XC8 Compiler
```bash
# Direct usage
xc8-cc --version

# Via Python wrapper (recommended)
xc8-wrapper --tool cc --cpu PIC16F877A --xc8-version 3.00
```

### Programming
```bash
# With ipecmd-wrapper
ipecmd-wrapper -P 16F877A -T PK3 -F build/main.hex

# Or with Python script
python upload.py
```

## Usage

### 1. Open in VS Code

1. Make sure you have VS Code with "Dev Containers" extension installed
2. Open this project in VS Code
3. Click "Reopen in Container" when VS Code prompts
4. Wait for the container to build (may take several minutes)

### 2. If build fails

1. Check your internet connection
2. Or use Docker manually (see below)

### 3. Test installation

```bash
# Check XC8 (after automatic installation)
xc8-cc --version

# Check xc8-wrapper
xc8-wrapper --version

# Compile example
cd examples/blink
xc8-wrapper --tool cc --xc8-version 3.00 --cpu PIC16F877A --source-dir . --main-c-file main.c
```

### 4. Development

The container includes all necessary tools for:
- Developing in C for PIC
- Modifying and testing xc8-wrapper
- Using debug and analysis tools

## Supported Microcontrollers

The XC8 compiler supports all 8-bit PICs, including:
- PIC10F, PIC12F, PIC16F, PIC18F families
- Popular examples: PIC16F877A, PIC18F4520, PIC12F675

## Troubleshooting

### Container won't build
- **Network issue**: Check your internet connection (XC8 download ~500MB)
- **Disk space**: Make sure you have enough space (~2GB)
- **Timeout**: XC8 download can be slow, try multiple times

**Quick solution**: Use Docker manually
```bash
docker build -t pic-dev .devcontainer/
docker run -it --rm -v ${PWD}:/workspace pic-dev
```

### XC8 not found after installation
```bash
# Check installation
ls -la /opt/microchip/bin/

# Add to PATH manually
export PATH="/opt/microchip/bin:$PATH"

# Or reinstall with script
bash .devcontainer/post-create.sh
```

### Compilation fails
- Check exact MCU name (case sensitive)
- Use `--verbose` for more details
- Consult XC8 documentation

### Programming issues
- **Hardware connection**: Ensure programmer is connected to host system
- **USB passthrough**: Docker may not have direct access to USB devices
- **Alternative**: Copy HEX files to host system for programming

### Docker permissions on Windows
```bash
# If permission issues on Windows
docker run --rm -it -v ${PWD}:/workspace -w /workspace ubuntu:22.04 bash
```

## Alternatives

### Docker Compose
```bash
# Development with docker-compose
docker-compose up xc8-dev

# Tests
docker-compose run test

# Compilation example
docker-compose run compile
```

### Manual XC8 installation
If automatic installation fails:

1. Download manually from [Microchip](https://www.microchip.com/en-us/tools-resources/develop/mplab-xc-compilers)
2. Copy the `.run` file into the container
3. Run manual installation

```bash
# In the container
sudo ./xc8-v3.00-full-install-linux-x64-installer.run --mode unattended --prefix /opt/microchip
```

## Programming from Container Limitations

⚠️ **Important**: Programming microcontrollers directly from dev containers has limitations:

1. **USB Access**: Docker containers may not have direct access to USB programmers
2. **Device Permissions**: Hardware programmers require specific permissions
3. **Host Integration**: Physical hardware is typically connected to the host system

**Recommended workflow**:
1. Develop and compile in the container
2. Copy generated HEX files to the host system
3. Use host-based programming tools (MPLAB X IPE, PICkit software)

## Resources

- [XC8 Documentation](https://www.microchip.com/en-us/tools-resources/develop/mplab-xc-compilers)
- [xc8-wrapper GitHub](https://github.com/s-celles/xc8-wrapper)
- [ipecmd-wrapper GitHub](https://github.com/s-celles/ipecmd-wrapper)
- [PIC Datasheets](https://www.microchip.com/en-us/products/microcontrollers-and-microprocessors/8-bit-mcus)
- [VS Code Dev Containers](https://code.visualstudio.com/docs/remote/containers)

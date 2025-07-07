# PIC 16F876A Project with XC8 v3.00

## Description
Demonstration project for PIC 16F876A with 4MHz crystal using XC8 v3.00 compiler.
The program blinks LEDs connected to uC.

## 📚 Documentation

**For complete documentation of the wrapper packages used in this project:**

- **XC8 Wrapper**: [https://s-celles.github.io/xc8-wrapper/](https://s-celles.github.io/xc8-wrapper/)
- **IPECMD Wrapper**: [https://s-celles.github.io/ipecmd-wrapper/](https://s-celles.github.io/ipecmd-wrapper/)

## Quick Start

1. **Install Prerequisites**: Python 3.x, XC8 v3.00, MPLAB X IDE
2. **Install Wrapper Packages**:
   ```bash
   pip install git+https://github.com/s-celles/xc8-wrapper.git
   pip install git+https://github.com/s-celles/ipecmd-wrapper.git
   ```
3. **Clone/Download** this project
4. **Compile**: `python compile.py`
5. **Upload**: `python upload.py` (with programmer connected)

## Project Structure
```
PIC_Test_Project/
├── src/
│   └── main.c              # Main source code
├── build/                  # Build output directory
├── compile.py              # Main compilation wrapper
├── upload.py               # Upload wrapper script
├── run_python.bat          # Batch file for easy execution
├── platformio.ini          # PlatformIO configuration (optional)
├── LICENSE                 # Project license (Apache 2.0)
└── README.md               # This file
```

## Hardware Configuration

### Required Components
- **Microcontroller**: PIC 16F876A
- **Crystal**: 4MHz
- **Capacitors**: 2x 22pF (for crystal)
- **LEDs**: 8 LEDs for PORTB
- **Resistors**: 8x 220-470Ω (current limiting for LEDs)
- **Capacitor**: 100nF (power supply decoupling)

## Usage

### Method 1: Python Build System (Recommended)
```bash
# Compile the project
python compile.py

# Program with PICkit3/PICkit4
python upload.py
```

### Method 2: Direct CLI Usage
```bash
# Compile with xc8-wrapper
xc8-wrapper --cpu PIC16F876A --xc8-version 3.00

# Upload with ipecmd-wrapper
ipecmd-wrapper -P 16F876A -T PK3 -F build/main.hex -W 5.0 --ipecmd-version 6.20
```

## Prerequisites

### Required Software
- **Python 3.x**: Required for build scripts
- **XC8 v3.00**: Microchip Compiler
- **MPLAB X IDE** (for programming)

### Programming Hardware
- **PICkit3**, **PICkit4**, or **PICkit5**
- **Programming socket** or development circuit
## Python Wrapper Packages

This project uses two modern Python wrapper packages for Microchip tools:

### XC8 Wrapper Package
- **Repository**: [github.com/s-celles/xc8-wrapper](https://github.com/s-celles/xc8-wrapper)
- **Documentation**: [s-celles.github.io/xc8-wrapper](https://s-celles.github.io/xc8-wrapper/)
- **Purpose**: Comprehensive wrapper for XC8 C compiler toolchain

### IPECMD Wrapper Package
- **Repository**: [github.com/s-celles/ipecmd-wrapper](https://github.com/s-celles/ipecmd-wrapper)
- **Documentation**: [s-celles.github.io/ipecmd-wrapper](https://s-celles.github.io/ipecmd-wrapper/)
- **Purpose**: Wrapper for MPLAB IPE command-line programming tool

## Installation

```bash
# Install both wrapper packages
pip install git+https://github.com/s-celles/xc8-wrapper.git
pip install git+https://github.com/s-celles/ipecmd-wrapper.git
```

## Important Legal Notice

**This project contains wrapper tools for Microchip's proprietary software:**

### Microchip Tools (NOT included)
- **XC8 Compiler** and **MPLAB X IDE** are proprietary software owned by Microchip Technology Inc.
- You must obtain proper licenses from Microchip to use these tools.

### License Summary
- **Wrapper Packages**: MIT License (open source)
- **This Project**: Apache 2.0 License (open source)
- **Microchip Tools**: Proprietary Microchip licenses (separate licensing required)

## Resources

- [XC8 Documentation](https://www.microchip.com/en-us/tools-resources/develop/mplab-xc-compilers)
- [PIC16F876A Datasheet](https://ww1.microchip.com/downloads/en/DeviceDoc/39582b.pdf)
- [MPLAB X IDE](https://www.microchip.com/en-us/tools-resources/develop/mplab-x-ide)

## License

This project is released under the **Apache 2.0 License**. See the LICENSE file for details.

**You are responsible for obtaining proper licenses for any Microchip tools you use with these wrappers.**

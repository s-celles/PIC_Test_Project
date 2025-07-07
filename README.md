# PIC 16F876A Project with XC8 v3.00

## Description
Demonstration project for PIC 16F876A with 4MHz crystal using XC8 v3.00 compiler.
The program blinks LEDs connected to uC.

## Quick Start

1. **Install Prerequisites**: Python 3.x, XC8 v3.00, MPLAB X IDE
2. **Clone/Download** this project
3. **Compile**: `python compile.py`
4. **Upload**: `python upload.py` (with programmer connected)

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

### Wiring Diagram
```
OSC1 ---- [4MHz Crystal] ---- OSC2
    |                       |
   [22pF]                  [22pF]
    |                       |
   GND                     GND

RB0-RB7 ---- [Resistor] ---- [LED] ---- VCC

VDD ---- [100nF] ---- VSS
VDD ---- +5V
VSS ---- GND
```

## Compilation and Programming

### Method 1: Python Build System (Recommended)
```bash
# Compile the project
python compile.py

# Or use the batch file (Windows)
.\run_python.bat compile

# Program with PICkit3/PICkit4
python upload.py

# Or use the batch file (Windows)
.\run_python.bat upload
```

### Method 2: Direct XC8 Toolchain Usage
```bash
# Compile with specific parameters
python xc8.py --xc8-version 3.00 --cpu PIC16F876A

# Upload with specific parameters
python upload.py --part 16F876A --tool PK3 --file build/main.hex
```

### Method 3: With PlatformIO (experimental)
```bash
pio run                    # Compile
pio run -t upload         # Program
```

## Prerequisites

### Required Software
- **Python 3.x**: Required for build scripts
- **XC8 v3.00**: Microchip Compiler
  - Path: `C:\Program Files\Microchip\xc8\v3.00\`
- **MPLAB X IDE** (for programming): 
  - Path: `C:\Program Files\Microchip\MPLABX\v6.20\`
- **PlatformIO** (optional): `pip install platformio`

### Programming Hardware
- **PICkit3**, **PICkit4**, or **PICkit5**
- **Programming socket** or development circuit

## Python Build System

### Configuration
All build configuration is centralized in `compile.py`:
- **XC8 Version**: `DEFAULT_XC8_VERSION = "3.00"`
- **Target CPU**: `DEFAULT_CPU = "PIC16F876A"`
- **Compilation flags**: Fully customizable in `XC8_COMPILE_FLAGS`
- **Linking flags**: Fully customizable in `XC8_LINK_FLAGS`

### Upload Configuration
Upload settings are in `upload.py`:
- **Default Tool**: `DEFAULT_TOOL = "PK3"`
- **Target Part**: `DEFAULT_PART = "16F876A"`
- **IPE Version**: `DEFAULT_IPECMD_VERSION = "6.20"`
- **HEX File**: `DEFAULT_HEX_FILE = "build\\main.hex"`

### Advanced Usage
```bash
# Compile with custom XC8 version
python xc8.py --xc8-version 3.00 --cpu PIC16F876A

# Upload with custom tool and settings
python upload.py --tool PK4 --part 16F876A --power 5.0 --verify P

# Use custom XC8 installation path
python xc8.py --xc8-path "C:\custom\xc8\bin\xc8-cc.exe" --cpu PIC16F876A
```

## Build System Architecture

The project uses a modular Python-based build system with modern Python packages:

### Core Scripts
- **`compile.py`**: Main build wrapper with all configuration constants
- **`upload.py`**: Upload wrapper that calls ipecmd-wrapper

### Python Packages
- **`xc8-wrapper`**: XC8 toolchain wrapper package (available at [github.com/s-celles/xc8-wrapper](https://github.com/s-celles/xc8-wrapper))
- **`ipecmd-wrapper`**: MPLAB IPE command-line wrapper package (available at [github.com/s-celles/ipecmd-wrapper](https://github.com/s-celles/ipecmd-wrapper))

### Key Features
- **Configurable**: All defaults as constants at the top of each script
- **Flexible**: Support for both version-based and path-based tool invocation
- **Cross-platform**: Python-based, works on Windows, Linux, macOS
- **Extensible**: Easy to add support for additional XC8 tools
- **Clean**: No hardcoded paths or values in tool wrappers
- **Modern**: Uses Python packages with proper CLI entry points

### Installation

This project uses two modern Python packages for toolchain interaction. These packages are available as separate repositories:

#### Option 1: Install from GitHub (Recommended)
```bash
# Install directly from GitHub repositories
pip install git+https://github.com/s-celles/xc8-wrapper.git
pip install git+https://github.com/s-celles/ipecmd-wrapper.git
```

#### Option 2: Development Installation
```bash
# Clone and install for development
git clone https://github.com/s-celles/xc8-wrapper.git
cd xc8-wrapper
pip install -e .

git clone https://github.com/s-celles/ipecmd-wrapper.git
cd ipecmd-wrapper
pip install -e .
```

After installation, you can use the CLI tools directly:
- `xc8-wrapper` - XC8 toolchain wrapper
- `ipecmd-wrapper` - MPLAB IPE command-line wrapper

### Package Information
- **xc8-wrapper**: [GitHub Repository](https://github.com/s-celles/xc8-wrapper)
- **ipecmd-wrapper**: [GitHub Repository](https://github.com/s-celles/ipecmd-wrapper)

## XC8 Wrapper Package (xc8-wrapper) - Complete Reference

The `xc8-wrapper` CLI tool is a comprehensive wrapper for the XC8 C compiler toolchain. It supports all major compilation and linking options through direct argument mapping.

**Package Repository**: [github.com/s-celles/xc8-wrapper](https://github.com/s-celles/xc8-wrapper)

### Installation
```bash
pip install git+https://github.com/s-celles/xc8-wrapper.git
```

### Basic Usage

```bash
xc8-wrapper --cpu PIC16F876A --xc8-version 3.00
```

### Advanced Usage with Direct Arguments

The xc8-wrapper supports all major xc8-cc.exe arguments directly:

```bash
# Optimization and debugging
xc8-wrapper --cpu PIC16F876A --xc8-version 3.00 -O2 --std c99 -v

# Preprocessor defines and includes
xc8-wrapper --cpu PIC16F876A --xc8-version 3.00 -D DEBUG=1 -D VERSION=2 -I ./include -I ./lib

# Memory and stack options
xc8-wrapper --cpu PIC16F876A --xc8-version 3.00 -mstack=compiled -mheap=100 --fill=0xFF

# Warning and error handling
xc8-wrapper --cpu PIC16F876A --xc8-version 3.00 -Werror -mwarn=3

# Library linking
xc8-wrapper --cpu PIC16F876A --xc8-version 3.00 -L./lib -lmath -lc

# Custom compilation and linking flags
xc8-wrapper --cpu PIC16F876A --xc8-version 3.00 --compile-flag "-Wall" --link-flag "-Wl,--defsym=__MPLAB_BUILD=1"
```

### Supported Argument Categories

The xc8-wrapper supports **80+ arguments** across all major xc8-cc.exe categories:

#### Preprocessor Options
- `-D, --define`: Define preprocessor symbols
- `-U, --undefine`: Undefine preprocessor symbols  
- `-I, --include`: Add include directories
- `-E, --preprocess-only`: Preprocess only
- `-H, --list-headers`: List included headers
- `-dM, --list-macros`: List defined macros
- `-C, --keep-comments`: Keep comments in preprocessed output

#### Compiler Options
- `-c, --compile-only`: Compile to object files only
- `-S, --assembly-only`: Generate assembly output
- `-v, --verbose`: Verbose compilation output
- `-w, --suppress-warnings`: Suppress all warnings
- `--save-temps`: Keep intermediate files
- `--std`: C language standard (c89, c90, c99, c11, etc.)
- `-ansi`: Use C90 standard

#### Optimization Options
- `-O, --optimize`: Optimization level (0, 1, 2, 3, g, s)
- `-flocal`: Local optimizations
- `-fcacheconst`: Cache constants optimization
- `-fasmfile`: Optimize assembler files

#### Warning and Error Options
- `-Wpedantic`: Flag non-standard keywords
- `-Werror`: Convert warnings to errors
- `-Wno-error`: Prevent warnings becoming errors

#### Library Options
- `-l, --library`: Link with library
- `-L, --library-path`: Add library search paths
- `-nostdlib`: Don't link standard library
- `-nostdinc`: Don't search standard includes
- `-nodefaultlibs`: Don't link default libraries
- `-nostartfiles`: Don't link startup files

#### Debug Options
- `-gdwarf-3`: Generate DWARF-3 debug info
- `-gcoff`: Generate COFF debug info
- `-ginhx32`: Generate Intel HEX output
- `-ginhx032`: Generate Intel HEX extended output

#### PIC-Specific Options
- `-maddrqual`: Address space qualifier handling
- `-mwarn`: Set warning level
- `-mstack`: Stack model and size
- `-mheap`: Maximum heap size
- `-msummary`: Compilation summary information
- `-mno-keep-startup`: Don't keep startup code
- `-mkeep-startup`: Keep startup code
- `-mno-default-config-bits`: Don't use default config bits
- `-mdefault-config-bits`: Use default config bits
- `-mno-download`: Don't make bootloader-compatible
- `-mdownload`: Make bootloader-compatible
- `-mchecksum`: Calculate and store checksum
- `-mcodeoffset`: Reset/interrupt vector offset
- `-mserial`: Insert serial number
- `-mreserve`: Reserve memory range
- `-mrom`: Adjust program memory ranges
- `-mram`: Adjust data memory ranges
- `-mdfp`: Select device family pack

#### Memory and Fill Options
- `--fill`: Fill unused memory with value
- `--memorysummary`: Create memory summary XML
- `--nofallback`: Don't fall back to lesser license modes

#### Data Type Options
- `-funsigned-char`: Default unsigned char
- `-fno-unsigned-char`: Default signed char
- `-fsigned-char`: Default signed char
- `-fno-signed-char`: Default unsigned char
- `-fshort-double`: 24-bit double precision
- `-fno-short-double`: 32-bit double precision
- `-fshort-float`: 24-bit float precision
- `-fno-short-float`: 32-bit float precision

#### Dependency Generation
- `-M`: Generate make dependencies
- `-MD`: Generate make dependencies (compile and deps)
- `-MF`: Generate dependencies to file
- `-MM`: Generate user header dependencies only
- `-MMD`: Generate user header dependencies (compile and deps)

#### Advanced/Custom Options
- `--compile-flag`: Add custom compilation flags
- `--link-flag`: Add custom linking flags

### Complete Options Reference

For a complete list of all available options, run:
```bash
xc8-wrapper --help
```

This will show all 80+ supported arguments with their descriptions.

## IPECMD Wrapper Package (ipecmd-wrapper) - Complete Reference

The `ipecmd-wrapper` CLI tool is a comprehensive wrapper for Microchip's MPLAB IPE command-line interface (IPECMD). It provides a user-friendly interface for programming PIC microcontrollers.

**Package Repository**: [github.com/s-celles/ipecmd-wrapper](https://github.com/s-celles/ipecmd-wrapper)

### Installation
```bash
pip install git+https://github.com/s-celles/ipecmd-wrapper.git
```

### Basic Usage

```bash
ipecmd-wrapper -P 16F876A -T PK3 -W 4.875 -F build/main.hex --ipecmd-version 6.20
```

### Advanced Usage

```bash
# Test programmer detection before programming
ipecmd-wrapper -P 16F876A -T PK3 -W 4.875 -F build/main.hex --ipecmd-version 6.20 --test-programmer

# Program with erase and verification
ipecmd-wrapper -P 16F876A -T PK3 -W 4.875 -F build/main.hex --ipecmd-version 6.20 -E -Y P

# Use custom IPECMD path
ipecmd-wrapper -P 16F876A -T PK3 -W 4.875 -F build/main.hex --ipecmd-path "C:\custom\path\ipecmd.exe"
```

### Supported Programmers

- **PK3**: PICkit 3
- **PK4**: PICkit 4
- **PK5**: PICkit 5
- **ICD3**: ICD 3
- **ICD4**: ICD 4
- **ICD5**: ICD 5
- **SNAP**: PICkit On Board (SNAP)
- **And more...**

## XC8 Wrapper Package Comprehensive Argument Support

The `xc8-wrapper` CLI tool provides complete support for all major XC8 compiler arguments, making it a professional-grade wrapper for the XC8 toolchain.

### Quick Examples

```bash
# Basic compilation with XC8 v3.00
xc8-wrapper --cpu PIC16F876A --xc8-version 3.00

# Advanced compilation with optimization and debugging
xc8-wrapper --cpu PIC16F876A --xc8-version 3.00 -O2 --std c99 -v -g

# Preprocessor definitions and includes
xc8-wrapper --cpu PIC16F876A --xc8-version 3.00 -D DEBUG=1 -D VERSION=100 -I ./include -I ./lib

# Memory optimization and PIC-specific options
xc8-wrapper --cpu PIC16F876A --xc8-version 3.00 -Os -mstack=compiled -mheap=64 --fill=0xFF

# Warning control and error handling
xc8-wrapper --cpu PIC16F876A --xc8-version 3.00 -Werror -Wpedantic -mwarn=3

# Library linking
xc8-wrapper --cpu PIC16F876A --xc8-version 3.00 -L./lib -lmath -lc
```

### Complete Argument Categories

#### 1. Preprocessor Options
- **`-D, --define`**: Define preprocessor symbols (`-D DEBUG=1 -D VERSION=2`)
- **`-U, --undefine`**: Undefine preprocessor symbols
- **`-I, --include`**: Add include directories (`-I ./include -I ./lib`)
- **`-E, --preprocess-only`**: Preprocess only
- **`-H, --list-headers`**: List included header files
- **`-dM, --list-macros`**: List all defined macros
- **`-C, --keep-comments`**: Keep comments in preprocessed output

#### 2. Compiler Control Options
- **`-c, --compile-only`**: Compile to object files only
- **`-S, --assembly-only`**: Generate assembly output
- **`-v, --verbose`**: Verbose compilation output
- **`-w, --suppress-warnings`**: Suppress all warnings
- **`--save-temps`**: Keep intermediate files
- **`--std`**: C language standard (`--std c99`, `--std c11`)
- **`-ansi`**: Use C90 standard

#### 3. Optimization Options
- **`-O, --optimize`**: Optimization level (`-O0`, `-O1`, `-O2`, `-O3`, `-Os`, `-Og`)
  - `-O0`: No optimization
  - `-O1`: Basic optimization
  - `-O2`: Default optimization (recommended)
  - `-O3`: Aggressive optimization (requires PRO license)
  - `-Os`: Size optimization
  - `-Og`: Debug-friendly optimization
- **`-flocal`**: Local optimizations
- **`-fcacheconst`**: Cache constants optimization
- **`-fasmfile`**: Optimize assembler files

#### 4. Warning and Error Control
- **`-Wpedantic`**: Flag non-standard keywords
- **`-Werror`**: Convert warnings to errors
- **`-Wno-error`**: Prevent warnings becoming errors

#### 5. Library and Linking Options
- **`-l, --library`**: Link with library (`-lmath -lc`)
- **`-L, --library-path`**: Add library search paths (`-L./lib`)
- **`-nostdlib`**: Don't link standard library
- **`-nostdinc`**: Don't search standard includes
- **`-nodefaultlibs`**: Don't link default libraries
- **`-nostartfiles`**: Don't link startup files

#### 6. Debug and Output Format Options
- **`-gdwarf-3`**: Generate DWARF-3 debug info
- **`-gcoff`**: Generate COFF debug info
- **`-ginhx32`**: Generate Intel HEX output
- **`-ginhx032`**: Generate Intel HEX extended output

#### 7. Data Type Control
- **`-funsigned-char`**: Default unsigned char
- **`-fno-unsigned-char`**: Default signed char
- **`-fsigned-char`**: Default signed char
- **`-fno-signed-char`**: Default unsigned char
- **`-fshort-double`**: 24-bit double precision
- **`-fno-short-double`**: 32-bit double precision
- **`-fshort-float`**: 24-bit float precision
- **`-fno-short-float`**: 32-bit float precision

#### 8. PIC-Specific Options
- **`-maddrqual`**: Address space qualifier handling (`-maddrqual=ignore`)
- **`-mwarn`**: Set warning level (`-mwarn=3`)
- **`-mstack`**: Stack model and size (`-mstack=compiled`)
- **`-mheap`**: Maximum heap size (`-mheap=64`)
- **`-msummary`**: Compilation summary information
- **`-mno-keep-startup`**: Don't keep startup code
- **`-mkeep-startup`**: Keep startup code
- **`-mno-default-config-bits`**: Don't use default config bits
- **`-mdefault-config-bits`**: Use default config bits
- **`-mno-download`**: Don't make bootloader-compatible
- **`-mdownload`**: Make bootloader-compatible
- **`-mchecksum`**: Calculate and store checksum
- **`-mcodeoffset`**: Reset/interrupt vector offset
- **`-mserial`**: Insert serial number
- **`-mreserve`**: Reserve memory range
- **`-mrom`**: Adjust program memory ranges
- **`-mram`**: Adjust data memory ranges
- **`-mdfp`**: Select device family pack

#### 9. Memory and Fill Options
- **`--fill`**: Fill unused memory with value (`--fill=0xFF`)
- **`--memorysummary`**: Create memory summary XML
- **`--nofallback`**: Don't fall back to lesser license modes

#### 10. Dependency Generation
- **`-M`**: Generate make dependencies
- **`-MD`**: Generate make dependencies (compile and deps)
- **`-MF`**: Generate dependencies to file
- **`-MM`**: Generate user header dependencies only
- **`-MMD`**: Generate user header dependencies (compile and deps)

#### 11. Advanced/Custom Options
- **`--compile-flag`**: Add custom compilation flags (`--compile-flag "-Wall"`)
- **`--link-flag`**: Add custom linking flags (`--link-flag "-Wl,--defsym=__MPLAB_BUILD=1"`)

### Real-World Usage Examples

```bash
# Production build with full optimization
xc8-wrapper --cpu PIC16F876A --xc8-version 3.00 \
  -O2 --std c99 \
  -D RELEASE=1 -D VERSION=100 \
  -mstack=compiled -mheap=32 \
  --fill=0xFF -ginhx032

# Debug build with verbose output
xc8-wrapper --cpu PIC16F876A --xc8-version 3.00 \
  -Og --std c99 \
  -D DEBUG=1 -D VERBOSE=1 \
  -v --save-temps \
  -gdwarf-3 -Wpedantic

# Library project build
xc8-wrapper --cpu PIC16F876A --xc8-version 3.00 \
  -O2 --std c99 \
  -I ./include -I ./common \
  -L ./lib -lmath -lutils \
  -mno-default-config-bits

# Size-optimized build for memory-constrained devices
xc8-wrapper --cpu PIC16F876A --xc8-version 3.00 \
  -Os --std c99 \
  -fshort-double -fshort-float \
  -mstack=compiled -mheap=16 \
  --fill=0x00
```

### Complete Options Reference

For the most up-to-date complete list of all 80+ supported arguments:
```bash
xc8-wrapper --help
```

This shows every available option with detailed descriptions, making the wrapper as comprehensive as using xc8-cc.exe directly.

## Important Legal Notice

**This project contains wrapper tools for Microchip's proprietary software:**

### Microchip Tools (NOT included in this project)
- **XC8 Compiler** (`xc8-cc.exe`, `xc8-ld.exe`, etc.)
- **MPLAB X IDE** and **MPLAB IPE** (`ipecmd.exe`)
- **All related Microchip development tools**

These tools are **proprietary software owned exclusively by Microchip Technology Inc.** and are subject to Microchip's own license terms. You must obtain proper licenses from Microchip to use these tools.

### This Project's Wrapper Code
The Python wrapper code used in this project is available as separate open source packages:
- **xc8-wrapper**: [GitHub Repository](https://github.com/s-celles/xc8-wrapper) (MIT License)
- **ipecmd-wrapper**: [GitHub Repository](https://github.com/s-celles/ipecmd-wrapper) (MIT License)

### License Summary
- **Wrapper Packages**: MIT License (open source)
- **This Project**: Apache 2.0 License (open source)
- **Microchip Tools**: Proprietary Microchip licenses (separate licensing required)

**You are responsible for obtaining proper licenses for any Microchip tools you use with these wrappers.**

## Resources

- [XC8 Documentation](https://www.microchip.com/en-us/tools-resources/develop/mplab-xc-compilers)
- [PIC16F876A Datasheet](https://ww1.microchip.com/downloads/en/DeviceDoc/39582b.pdf)
- [MPLAB X IDE](https://www.microchip.com/en-us/tools-resources/develop/mplab-x-ide)
- [PlatformIO PIC](https://docs.platformio.org/)

## License

**This project uses wrapper tools for Microchip's proprietary software. Please read the licensing information carefully:**

### This Project License
This PIC test project is released under the **Apache 2.0 License**. See the LICENSE file for details.

### Wrapper Packages License
The Python wrapper packages used in this project are available as separate open source packages:
- **xc8-wrapper**: [GitHub Repository](https://github.com/s-celles/xc8-wrapper) (MIT License)
- **ipecmd-wrapper**: [GitHub Repository](https://github.com/s-celles/ipecmd-wrapper) (MIT License)

### Microchip Tools License
The underlying tools (XC8 compiler, MPLAB X IDE, MPLAB IPE, etc.) are **proprietary software owned exclusively by Microchip Technology Inc.** and are subject to Microchip's own license terms. You must obtain proper licenses from Microchip to use these tools.

**You are responsible for obtaining proper licenses for any Microchip tools you use with these wrappers.**

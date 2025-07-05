#!/usr/bin/env python3
"""
Simple compilation wrapper that calls xc8-wrapper with default arguments
"""

import sys
import subprocess
import os
import argparse
from pathlib import Path
from colorama import init, Fore, Style

# Initialize colorama for cross-platform support
init(autoreset=True)

# Version information
__version__ = "0.1.0"


def print_colored(text: str, color: str) -> None:
    """Print text with specified color using colorama"""
    print(f"{color}{text}{Style.RESET_ALL}")


# Color constants
class Colors:
    CYAN = Fore.CYAN
    GREEN = Fore.GREEN
    YELLOW = Fore.YELLOW
    RED = Fore.RED
    GRAY = Fore.LIGHTBLACK_EX

# =============================================================================
# CONFIGURATION CONSTANTS - Modify these to change default behavior
# =============================================================================

# Default compilation arguments
DEFAULT_XC8_VERSION = "3.00"
DEFAULT_CPU = "PIC16F876A"

# Build configuration
BUILD_DIR = "build"
SOURCE_DIR = "src"
MAIN_C_FILE = "main.c"
OUTPUT_HEX = "main.hex"
OUTPUT_ELF = "main.elf"
OUTPUT_P1 = "main.p1"
OUTPUT_MAP = "main.map"
MEMORY_FILE = "memoryfile.xml"

# XC8 Compilation flags
XC8_COMPILE_FLAGS = [
    "-c",  # Compile to object file
    "-fno-short-double",  # 32-bit doubles
    "-fno-short-float",  # 32-bit floats
    "-O2",  # Optimization level 2
    "-fasmfile",  # Generate assembly file
    "-maddrqual=ignore",  # Address qualifier handling
    "-xassembler-with-cpp",  # Preprocess assembly files
    "-mwarn=-3",  # Warning level
    "-Wa,-a",  # Assembler options
    "-DXPRJ_default=default",  # Define project macro
    "-msummary=-psect,-class,+mem,-hex,-file",  # Summary options
    "-ginhx032",  # Generate Intel HEX
    "-Wl,--data-init",  # Initialize data
    "-mno-keep-startup",  # Don't keep startup code
    "-mno-download",  # No download mode
    "-mno-default-config-bits",  # No default config bits
    "-std=c99",  # C99 standard
    "-gdwarf-3",  # Debug format
    "-mstack=compiled:auto:auto:auto",  # Stack configuration
]

# XC8 Linking flags - modify these to change linking behavior
XC8_LINK_FLAGS = [
    "-DXPRJ_default=default",  # Define project macro
    "-Wl,--defsym=__MPLAB_BUILD=1",  # MPLAB build symbol
    "-fno-short-double",  # 32-bit doubles
    "-fno-short-float",  # 32-bit floats
    "-O2",  # Optimization level 2
    "-fasmfile",  # Generate assembly file
    "-maddrqual=ignore",  # Address qualifier handling
    "-xassembler-with-cpp",  # Preprocess assembly files
    "-mwarn=-3",  # Warning level
    "-Wa,-a",  # Assembler options
    "-msummary=-psect,-class,+mem,-hex,-file",  # Summary options
    "-ginhx032",  # Generate Intel HEX
    "-Wl,--data-init",  # Initialize data
    "-mno-keep-startup",  # Don't keep startup code
    "-mno-download",  # No download mode
    "-mno-default-config-bits",  # No default config bits
    "-std=c99",  # C99 standard
    "-gdwarf-3",  # Debug format
    "-mstack=compiled:auto:auto:auto",  # Stack configuration
]


def main():
    """Call xc8-wrapper with default arguments"""
    # Parse command line arguments
    parser = argparse.ArgumentParser(
        description="Simple compilation wrapper that calls xc8-wrapper with default arguments",
        prog="compile.py"
    )
    
    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {__version__}"
    )
    
    args = parser.parse_args()
    
    print_colored("=== COMPILE WRAPPER ===", Colors.CYAN)

    # Use the installed xc8-wrapper command
    xc8_command = "xc8-wrapper"

    # Call xc8-wrapper with default arguments defined in this script
    cmd = [
        xc8_command,
        "--xc8-version",
        DEFAULT_XC8_VERSION,
        "--cpu",
        DEFAULT_CPU,
    ]

    # Add compilation flags - each flag as a separate argument using equals format
    for flag in XC8_COMPILE_FLAGS:
        cmd.append(f"--compile-flag={flag}")

    # Add linking flags - each flag as a separate argument using equals format
    for flag in XC8_LINK_FLAGS:
        cmd.append(f"--link-flag={flag}")

    print_colored(f"Calling xc8-wrapper with default arguments:", Colors.YELLOW)
    print_colored(f"  - XC8 Version: {DEFAULT_XC8_VERSION}", Colors.GRAY)
    print_colored(f"  - Target CPU: {DEFAULT_CPU}", Colors.GRAY)
    print_colored(f"  - Compile Flags: {len(XC8_COMPILE_FLAGS)} flags", Colors.GRAY)
    print_colored(f"  - Link Flags: {len(XC8_LINK_FLAGS)} flags", Colors.GRAY)
    print_colored(
        f"Command: {' '.join(cmd[:6])}... (total {len(cmd)} args)", Colors.CYAN
    )

    try:
        # Run xc8-wrapper and pass through its exit code
        result = subprocess.run(cmd, check=False)
        sys.exit(result.returncode)

    except Exception as e:
        print_colored(f"✗ Error running xc8-wrapper: {e}", Colors.RED)
        sys.exit(1)


if __name__ == "__main__":
    main()

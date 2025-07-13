#!/usr/bin/env python3
"""
Simple compilation wrapper that calls xc8-wrapper with default arguments
"""

import typer
from logger import log
from xc8_wrapper.core import handle_cc_tool

# Version information
__version__ = "0.1.0"


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


# Create the Typer app
app = typer.Typer(
    help="Simple compilation wrapper that calls xc8-wrapper with default arguments"
)


def version_callback(value: bool):
    """Show version information"""
    if value:
        typer.echo(f"compile.py {__version__}")
        raise typer.Exit()


@app.command()
def main(
    version: bool = typer.Option(
        False,
        "--version",
        callback=version_callback,
        is_eager=True,
        help="Show version and exit",
    ),
):
    """Call xc8-wrapper with default arguments"""
    log.info("=== COMPILE WRAPPER ===")

    # Create arguments object that mimics what xc8-wrapper CLI would create
    class Args:
        def __init__(self):
            # Required arguments
            self.cpu = DEFAULT_CPU
            self.xc8_version = DEFAULT_XC8_VERSION
            self.xc8_path = None

            # Compilation and linking flags
            self.compile_flag = XC8_COMPILE_FLAGS
            self.link_flag = XC8_LINK_FLAGS

            # Preprocessor arguments
            self.define = None
            self.undefine = None
            self.include = None
            self.keep_comments = False
            self.preprocess_only = False
            self.list_headers = False
            self.list_macros = False

            # Compiler mode arguments
            self.compile_only = False
            self.assembly_only = False
            self.verbose = False
            self.suppress_warnings = False
            self.save_temps = False

            # Optimization arguments
            self.optimize = None

            # Language standard arguments
            self.std = None

            # File and directory arguments
            self.build_dir = BUILD_DIR
            self.source_dir = SOURCE_DIR
            self.main_c_file = MAIN_C_FILE
            self.output_hex = OUTPUT_HEX
            self.output_elf = OUTPUT_ELF
            self.output_p1 = OUTPUT_P1
            self.output_map = OUTPUT_MAP
            self.memory_file = MEMORY_FILE

    args = Args()

    log.info("Calling xc8-wrapper with default arguments:")
    log.debug(f"  - XC8 Version: {DEFAULT_XC8_VERSION}")
    log.debug(f"  - Target CPU: {DEFAULT_CPU}")
    log.debug(f"  - Compile Flags: {len(XC8_COMPILE_FLAGS)} flags")
    log.debug(f"  - Link Flags: {len(XC8_LINK_FLAGS)} flags")

    try:
        # Call xc8_wrapper directly instead of using subprocess
        handle_cc_tool(args)
        log.info("✓ Compilation completed successfully")

    except SystemExit as e:
        if e.code != 0:
            log.error(f"✗ Compilation failed with exit code {e.code}")
            raise typer.Exit(e.code)
    except Exception as e:
        log.error(f"✗ Error during compilation: {e}")
        raise typer.Exit(1)


if __name__ == "__main__":
    app()

#!/usr/bin/env python3
"""
Upload script for PIC microcontrollers
This script calls ipecmd-wrapper
"""

from pathlib import Path
import typer
from logger import log

# Import ipecmd_wrapper directly to avoid subprocess
from ipecmd_wrapper.core import program_pic

# Version information
__version__ = "0.1.0"


# Args class to mimic argument structure for ipecmd_wrapper.core.program_pic
class Args:
    """Simple namespace class to hold upload arguments"""

    def __init__(
        self,
        part: str,
        tool: str,
        file: str,
        ipecmd_version: str = None,
        ipecmd_path: str = None,
        power: str = "5.0",
        test_programmer: bool = False,
        erase: bool = False,
        verify: str = "",
        memory: str = "",
        vdd_first: bool = False,
        logout: bool = True,  # Default to True for upload script
    ):
        self.part = part
        self.tool = tool
        self.file = file
        self.ipecmd_version = ipecmd_version
        self.ipecmd_path = ipecmd_path
        self.power = power
        self.test_programmer = test_programmer
        self.erase = erase
        self.verify = verify
        self.memory = memory
        self.vdd_first = vdd_first
        self.logout = logout


# Default values for CLI arguments
DEFAULT_PART = "16F876A"
DEFAULT_TOOL = "PK3"
DEFAULT_IPECMD_VERSION = "6.20"
DEFAULT_POWER = "4.875"
DEFAULT_HEX_FILE = Path("build/main.hex")
DEFAULT_TEST_PROGRAMMER = False
DEFAULT_ERASE = False
DEFAULT_VERIFY = ""
DEFAULT_IPECMD_PATH = ""


# Create the Typer app
app = typer.Typer(help="Upload script for PIC microcontrollers")


def version_callback(value: bool):
    """Show version information"""
    if value:
        typer.echo(f"upload.py {__version__}")
        raise typer.Exit()


@app.command()
def main(
    part: str = typer.Option(
        DEFAULT_PART, "--part", help=f"Target PIC part (default: {DEFAULT_PART})"
    ),
    tool: str = typer.Option(
        DEFAULT_TOOL, "--tool", help=f"Programming tool (default: {DEFAULT_TOOL})"
    ),
    ipecmd_version: str = typer.Option(
        DEFAULT_IPECMD_VERSION,
        "--ipecmd-version",
        help=f"MPLAB IPE version to use (default: {DEFAULT_IPECMD_VERSION})",
    ),
    ipecmd_path: str = typer.Option(
        DEFAULT_IPECMD_PATH,
        "--ipecmd-path",
        help="Full path to ipecmd.exe (overrides --ipecmd-version)",
    ),
    power: str = typer.Option(
        DEFAULT_POWER,
        "--power",
        help=f"Power target from tool (VDD voltage, default: {DEFAULT_POWER})",
    ),
    file: str = typer.Option(
        str(DEFAULT_HEX_FILE),
        "--file",
        help=f"Hex file to upload (default: {DEFAULT_HEX_FILE})",
    ),
    test_programmer: bool = typer.Option(
        DEFAULT_TEST_PROGRAMMER,
        "--test-programmer",
        help="Test programmer detection before programming",
    ),
    erase: bool = typer.Option(
        DEFAULT_ERASE, "--erase", help="Erase Flash Device before programming"
    ),
    verify: str = typer.Option(
        DEFAULT_VERIFY,
        "--verify",
        help="Verify Device memory regions (P=Program, E=EEPROM, I=ID, C=Configuration, B=Boot, A=Auxiliary)",
    ),
    version: bool = typer.Option(
        False,
        "--version",
        callback=version_callback,
        is_eager=True,
        help="Show version and exit",
    ),
):
    """Upload HEX file to PIC microcontroller using ipecmd-wrapper"""
    log.info("=== UPLOAD HEX FILE TO PIC ===")

    # Create Args object for ipecmd_wrapper.core.program_pic
    args = Args(
        part=part,
        tool=tool,
        file=file,
        ipecmd_version=ipecmd_version if not ipecmd_path else None,
        ipecmd_path=ipecmd_path if ipecmd_path else None,
        power=power,
        test_programmer=test_programmer,
        erase=erase,
        verify=verify,
        logout=True,  # Always logout after programming
    )

    log.debug(f"Programming PIC {part} with {tool} using {file}")

    try:
        # Call ipecmd_wrapper directly instead of subprocess
        program_pic(args)
        log.info("✓ Upload successful")
    except SystemExit as e:
        if e.code != 0:
            log.error(f"✗ Upload failed with exit code {e.code}")
            raise typer.Exit(e.code)
        else:
            log.info("✓ Upload successful")
    except Exception as e:
        log.error(f"✗ Error running upload: {e}")
        raise typer.Exit(1)


if __name__ == "__main__":
    app()

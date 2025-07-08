#!/usr/bin/env python3
"""
Upload script for PIC microcontrollers
This script calls ipecmd-wrapper
"""

import os
from pathlib import Path
import sys
import subprocess
import argparse
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
    RED = Fore.RED
    GRAY = Fore.LIGHTBLACK_EX


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


def main():
    print_colored("=== UPLOAD HEX FILE TO PIC ===", Colors.CYAN)

    # Command line arguments
    parser = argparse.ArgumentParser(
        description="Upload script for PIC microcontrollers", prog="upload.py"
    )

    parser.add_argument(
        "--version", action="version", version=f"%(prog)s {__version__}"
    )
    parser.add_argument(
        "--part",
        default=DEFAULT_PART,
        help=f"Target PIC part (default: {DEFAULT_PART})",
    )
    parser.add_argument(
        "--tool",
        default=DEFAULT_TOOL,
        help=f"Programming tool (default: {DEFAULT_TOOL})",
    )
    parser.add_argument(
        "--ipecmd-version",
        default=DEFAULT_IPECMD_VERSION,
        help=f"MPLAB IPE version to use (default: {DEFAULT_IPECMD_VERSION})",
    )
    parser.add_argument(
        "--ipecmd-path",
        default=DEFAULT_IPECMD_PATH,
        help="Full path to ipecmd.exe (overrides --ipecmd-version)",
    )
    parser.add_argument(
        "--power",
        default=DEFAULT_POWER,
        help=f"Power target from tool (VDD voltage, default: {DEFAULT_POWER})",
    )
    parser.add_argument(
        "--file",
        default=str(DEFAULT_HEX_FILE),
        help=f"Hex file to upload (default: {DEFAULT_HEX_FILE})",
    )
    parser.add_argument(
        "--test-programmer",
        action="store_true",
        default=DEFAULT_TEST_PROGRAMMER,
        help="Test programmer detection before programming",
    )
    parser.add_argument(
        "--erase",
        action="store_true",
        default=DEFAULT_ERASE,
        help="Erase Flash Device before programming",
    )
    parser.add_argument(
        "--verify",
        default=DEFAULT_VERIFY,
        help="Verify Device memory regions (P=Program, E=EEPROM, I=ID, C=Configuration, B=Boot, A=Auxiliary)",
    )

    args = parser.parse_args()

    # Build the ipecmd command using the ipecmd_wrapper package
    upload_cmd = [
        "ipecmd-wrapper",
        "-P",
        args.part,
        "-T",
        args.tool,
        "-W",
        args.power,
        "-F",
        args.file,
        "-OL",  # Always logout after programming
    ]

    # Add either ipecmd-path or version
    if args.ipecmd_path:
        upload_cmd.extend(["--ipecmd-path", args.ipecmd_path])
    else:
        upload_cmd.extend(["--ipecmd-version", args.ipecmd_version])

    # Add optional arguments
    if args.test_programmer:
        upload_cmd.append("--test-programmer")

    if args.erase:
        upload_cmd.append("-E")

    if args.verify:
        upload_cmd.extend(["-Y", args.verify])

    print_colored(f"Running: {' '.join(upload_cmd)}", Colors.GRAY)

    try:
        result = subprocess.run(upload_cmd)
        if result.returncode == 0:
            print_colored("\n[OK] Upload successful", Colors.GREEN)
        else:
            print_colored(
                f"\n[ERROR] Upload failed with return code {result.returncode}", Colors.RED
            )
            sys.exit(result.returncode)
    except Exception as e:
        print_colored(f"\n[ERROR] Error running upload: {e}", Colors.RED)
        sys.exit(1)


if __name__ == "__main__":
    main()

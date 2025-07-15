#!/bin/bash
# Wrapper script for ipecmd.jar in a Linux environment
#
# This script is used to run ipecmd.jar from the command line
#
# Usage:
#
# Microchip MPLAB X IDE must be installed, and the path to ipecmd.jar should be correct.
# You can run this script with any arguments you would normally pass to ipecmd.jar.
#
# Example:
#
# ./ipecmd.sh -?  # Displays help information
# ./ipecmd.sh -c -p /dev/ttyUSB0 -b 115200 -f /home/user/my_project/my_project.hex
#
# Usage in Python script:
#
# python3 upload.py --ipecmd-path="./ipecmd.sh"

java -jar /opt/microchip/mplabx/v6.20/mplab_platform/mplab_ipe/ipecmd.jar "$@"


#!/usr/bin/env pwsh
# Wrapper script for ipecmd.jar in a Windows environment
#
# This script is used to run ipecmd.jar from the command line
#
# Usage:
#
# Microchip MPLAB X IDE must be installed, and the path to ipecmd.jar should be correct.
# You can run this script with any arguments you would normally pass to ipecmd.jar.
#
# Example:
# ./ipecmd.sh -?  # Displays help information
# ./ipecmd.ps1 -P PIC16F877A -T PK3 -F build\main.hex -M -OL
#
# Usage in Python script:
#
# python upload.py --ipecmd-path=".\ipecmd.ps1"

# Path to ipecmd.jar
$ipecmdPath = "C:\Program Files\Microchip\MPLABX\v6.20\mplab_platform\mplab_ipe\ipecmd.jar"

# Check if ipecmd.jar exists
if (-not (Test-Path $ipecmdPath)) {
    Write-Host "Error: ipecmd.jar not found at: $ipecmdPath" -ForegroundColor Red
    Write-Host "Please check that MPLAB X IDE v6.20 is installed correctly." -ForegroundColor Yellow
    exit 1
}

# Check if Java is available
try {
    $javaVersion = java -version 2>&1
    if ($LASTEXITCODE -ne 0) {
        throw "Java not found"
    }
} catch {
    Write-Host "Error: Java not found in PATH" -ForegroundColor Red
    Write-Host "Please install Java or add it to your PATH." -ForegroundColor Yellow
    exit 1
}

# Run ipecmd.jar with all passed arguments
Write-Host "Running ipecmd with arguments: $args" -ForegroundColor Green
java -jar "$ipecmdPath" @args

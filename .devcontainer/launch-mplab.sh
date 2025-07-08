#!/bin/bash

# Helper script to launch MPLAB X IDE in the devcontainer

echo "🚀 MPLAB X IDE Launcher"
echo "======================="

# Check prerequisites
echo "🔍 Checking environment..."

# Check Java
if ! command -v java &> /dev/null; then
    echo "❌ Java not found! MPLAB X requires at least Java 8."
    exit 1
fi

# Check MPLAB X
if [ ! -f "/opt/microchip/mplabx/v6.25/mplab_platform/bin/mplab_ide" ]; then
    echo "❌ MPLAB X IDE not found in /opt/microchip/mplabx/v6.25/"
    exit 1
fi

# Check X11
if [ -z "$DISPLAY" ]; then
    echo "⚠️  DISPLAY variable not set."
    echo "   For GUI support, configure X11 forwarding:"
    echo "   - Linux: xhost +local:docker && export DISPLAY=:0"
    echo "   - macOS: Install XQuartz and configure DISPLAY"
    echo "   - Windows: Use VcXsrv or X410"
    echo ""
fi

echo "✅ Java version:"
java -version 2>&1 | head -1

echo "✅ MPLAB X found: /opt/microchip/mplabx/v6.25/"

echo ""
echo "🎯 Launch options:"
echo "  1. Graphical interface (requires X11)"
echo "  2. Command line help"
echo "  3. Version and information"

read -p "Choose an option (1-3): " choice

case $choice in
    1)
        echo "🖥️  Launching MPLAB X IDE (graphical interface)..."
        export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
        exec /opt/microchip/mplabx/v6.25/mplab_platform/bin/mplab_ide
        ;;
    2)
        echo "📖 MPLAB X IDE help:"
        /opt/microchip/mplabx/v6.25/mplab_platform/bin/mplab_ide --help
        ;;
    3)
        echo "ℹ️  MPLAB X information:"
        echo "   Path: /opt/microchip/mplabx/v6.25/"
        echo "   Version: 6.25"
        echo "   Java: $(java -version 2>&1 | head -1)"
        ;;
    *)
        echo "❌ Invalid option"
        exit 1
        ;;
esac

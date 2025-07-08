#!/bin/bash

# Post-creation script for PIC devcontainer (XC8 only)
echo "🚀 Setting up PIC development environment..."

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to display colored messages
print_status() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Update pip and install basic Python packages
print_status "Installing basic Python packages..."
python3 -m pip install --upgrade pip
pip3 install colorama setuptools wheel

# Install development dependencies
print_status "Installing development dependencies..."
python3 -m pip install --user \
    pytest \
    pytest-cov \
    black \
    flake8 \
    pylint \
    mypy

# Install XC8 if not already present
print_status "Checking XC8 installation..."
if [ ! -f "/opt/microchip/bin/xc8-cc" ]; then
    print_status "Installing XC8 Compiler..."
    cd /tmp
    
    # Download XC8 with error handling
    if wget -q --timeout=60 --tries=2 \
        "https://ww1.microchip.com/downloads/aemDocuments/documents/DEV/ProductDocuments/SoftwareTools/xc8-v3.00-full-install-linux-x64-installer.run"; then
        
        print_status "Download completed, installing..."
        chmod +x xc8-v3.00-full-install-linux-x64-installer.run
        
        # Install with proper parameters
        echo "y" | sudo ./xc8-v3.00-full-install-linux-x64-installer.run --mode unattended --unattendedmodeui none --netservername localhost --LicenseType FreeMode --prefix /opt/microchip
        
        # Cleanup
        rm -f xc8-v3.00-full-install-linux-x64-installer.run
        
        print_success "XC8 installed successfully"
    else
        print_error "Failed to download XC8"
        print_warning "You can install XC8 manually later"
    fi
else
    print_success "XC8 already installed"
fi

# Install wrapper packages from local directories
print_status "Installing wrapper packages..."
if [ -d "./xc8-wrapper" ]; then
    pip3 install -e ./xc8-wrapper
    print_success "xc8-wrapper installed"
else
    print_warning "xc8-wrapper directory not found"
fi

if [ -d "./ipecmd-wrapper" ]; then
    pip3 install -e ./ipecmd-wrapper
    print_success "ipecmd-wrapper installed"
else
    print_warning "ipecmd-wrapper directory not found"
fi

# Check XC8 installation
print_status "Verifying XC8 installation..."
if [ -f "/opt/microchip/bin/xc8-cc" ]; then
    print_success "XC8 Compiler found: /opt/microchip/bin/xc8-cc"
    /opt/microchip/bin/xc8-cc --version | head -3 2>/dev/null || print_warning "XC8 version check failed"
else
    print_error "XC8 Compiler not found!"
fi

# Test wrapper packages
print_status "Testing wrapper packages..."
if command -v xc8-wrapper &> /dev/null; then
    print_success "xc8-wrapper CLI available"
    xc8-wrapper --version 2>/dev/null || print_warning "xc8-wrapper version check failed"
else
    print_warning "xc8-wrapper CLI not available"
fi

if command -v ipecmd-wrapper &> /dev/null; then
    print_success "ipecmd-wrapper CLI available"
    ipecmd-wrapper --version 2>/dev/null || print_warning "ipecmd-wrapper version check failed"
else
    print_warning "ipecmd-wrapper CLI not available"
fi

# Create useful symbolic links
print_status "Creating symbolic links..."
sudo ln -sf /opt/microchip/bin/xc8-cc /usr/local/bin/xc8-cc 2>/dev/null || true

# Display environment information
print_status "Environment information:"
echo "  - XC8 Path: /opt/microchip/bin"
echo "  - Python: $(python3 --version)"
echo ""
print_status "Available commands:"
echo "  - xc8-wrapper : Wrapper for XC8 compiler"
echo "  - ipecmd-wrapper : Wrapper for programming tool"
echo "  - python compile.py : Compile PIC project"
echo "  - python upload.py : Program microcontroller"

print_success "Environment setup completed! 🎉"

#!/bin/bash

# Troubleshooting script for devcontainer issues

echo "🔍 DevContainer Troubleshooting"
echo "================================"

# Option 1: Use simple configuration
echo ""
echo "Option 1: Use simplified devcontainer"
echo "-------------------------------------"
echo "If your devcontainer is broken, try using the simplified version:"
echo ""
echo "1. Backup current config:"
echo "   mv .devcontainer/devcontainer.json .devcontainer/devcontainer.json.backup"
echo ""
echo "2. Use simple config:"
echo "   cp .devcontainer/devcontainer.simple.json .devcontainer/devcontainer.json"
echo ""
echo "3. Use simple Dockerfile:"
echo "   mv .devcontainer/Dockerfile .devcontainer/Dockerfile.backup"
echo "   cp .devcontainer/Dockerfile.simple .devcontainer/Dockerfile"
echo ""
echo "4. Use simple post-create script:"
echo "   mv .devcontainer/post-create.sh .devcontainer/post-create.sh.backup"
echo "   cp .devcontainer/post-create.simple.sh .devcontainer/post-create.sh"
echo "   chmod +x .devcontainer/post-create.sh"

# Option 2: Manual Docker build
echo ""
echo "Option 2: Manual Docker build"
echo "------------------------------"
echo "If VS Code devcontainer fails, try manual Docker:"
echo ""
echo "1. Build manually:"
echo "   docker build -t pic-dev .devcontainer/"
echo ""
echo "2. Run manually:"
echo "   docker run -it --rm -v \"\$(pwd):/workspaces/pic-project\" pic-dev"

# Option 3: Check common issues
echo ""
echo "Option 3: Common issues to check"
echo "---------------------------------"
echo "1. Docker Desktop is running"
echo "2. VS Code has 'Dev Containers' extension installed"
echo "3. No syntax errors in devcontainer.json"
echo "4. Dockerfile exists and is valid"
echo "5. Windows: Make sure Docker uses Linux containers"

# Option 4: Clean slate
echo ""
echo "Option 4: Clean slate approach"
echo "------------------------------"
echo "1. Clean Docker:"
echo "   docker system prune -a"
echo ""
echo "2. Remove VS Code container cache:"
echo "   # Close VS Code first, then:"
echo "   # Delete: %APPDATA%\\Code\\User\\globalStorage\\ms-vscode-remote.remote-containers"
echo ""
echo "3. Restart Docker Desktop"
echo "4. Restart VS Code"

echo ""
echo "🆘 If all else fails:"
echo "   - Check VS Code Output panel for detailed errors"
echo "   - Try opening a simpler project first to test devcontainers"
echo "   - Consider using docker-compose instead: 'make build && make run'"

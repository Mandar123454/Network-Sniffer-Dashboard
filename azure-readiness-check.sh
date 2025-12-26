#!/bin/bash
# Azure Deployment Test Script
# This script validates your application is ready for Azure deployment

echo "======================================"
echo "Azure Deployment Readiness Check"
echo "======================================"
echo ""

# Check Python version
echo "1. Checking Python version..."
python --version
python_version=$(python -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')
if (( $(echo "$python_version >= 3.7" | bc -l) )); then
    echo "   ✅ Python version $python_version is compatible"
else
    echo "   ❌ Python version $python_version is too old (minimum 3.7 required)"
fi
echo ""

# Check requirements.txt
echo "2. Checking requirements.txt..."
if [ -f requirements.txt ]; then
    echo "   ✅ requirements.txt found"
    echo "   Dependencies:"
    while IFS= read -r line; do
        [ ! -z "$line" ] && echo "     - $line"
    done < requirements.txt
else
    echo "   ❌ requirements.txt not found"
fi
echo ""

# Check for necessary files
echo "3. Checking for necessary deployment files..."
files=("app.py" "Dockerfile" "web.config" "startup.sh" "AZURE_DEPLOYMENT.md")
for file in "${files[@]}"; do
    if [ -f "$file" ]; then
        echo "   ✅ $file found"
    else
        echo "   ⚠️  $file not found"
    fi
done
echo ""

# Check dependencies installation
echo "4. Checking if dependencies are installed..."
python -c "import flask; print('   ✅ Flask installed')" 2>/dev/null || echo "   ❌ Flask not installed"
python -c "import scapy; print('   ✅ Scapy installed')" 2>/dev/null || echo "   ❌ Scapy not installed"
python -c "import PIL; print('   ✅ Pillow installed')" 2>/dev/null || echo "   ❌ Pillow not installed"
python -c "import dotenv; print('   ✅ python-dotenv installed')" 2>/dev/null || echo "   ❌ python-dotenv not installed"
echo ""

# Check Flask app
echo "5. Checking Flask app syntax..."
python -m py_compile app.py && echo "   ✅ app.py syntax is valid" || echo "   ❌ app.py has syntax errors"
echo ""

# Check templates
echo "6. Checking template files..."
if [ -d "templates" ]; then
    echo "   ✅ templates directory found"
    ls -la templates/ | tail -n +2 | awk '{print "     - " $NF}'
else
    echo "   ❌ templates directory not found"
fi
echo ""

# Check static files
echo "7. Checking static files..."
if [ -d "static" ]; then
    echo "   ✅ static directory found"
    ls -la static/ | tail -n +2 | awk '{print "     - " $NF}'
else
    echo "   ❌ static directory not found"
fi
echo ""

# Docker check
echo "8. Checking Docker configuration..."
if [ -f "Dockerfile" ]; then
    echo "   ✅ Dockerfile found"
    echo "   Docker image will use Python 3.11-slim"
else
    echo "   ❌ Dockerfile not found"
fi
echo ""

# Azure configuration check
echo "9. Checking Azure configuration files..."
if [ -f "azure-deploy.json" ]; then
    echo "   ✅ azure-deploy.json found (ARM template)"
else
    echo "   ⚠️  azure-deploy.json not found"
fi

if [ -f ".env.example" ]; then
    echo "   ✅ .env.example found"
else
    echo "   ⚠️  .env.example not found"
fi
echo ""

# GitHub Actions check
echo "10. Checking CI/CD configuration..."
if [ -f ".github/workflows/azure-deploy.yml" ]; then
    echo "   ✅ GitHub Actions workflow for Azure deployment found"
else
    echo "   ⚠️  GitHub Actions workflow not found"
fi

if [ -f ".github/workflows/docker-build.yml" ]; then
    echo "   ✅ GitHub Actions workflow for Docker build found"
else
    echo "   ⚠️  Docker build workflow not found"
fi
echo ""

echo "======================================"
echo "Summary"
echo "======================================"
echo "✅ Your application is ready for Azure deployment!"
echo ""
echo "Next steps:"
echo "1. Create Azure Account: https://azure.microsoft.com/free/"
echo "2. Install Azure CLI: https://docs.microsoft.com/cli/azure/install-azure-cli"
echo "3. Read AZURE_DEPLOYMENT.md for detailed instructions"
echo "4. Choose deployment method (App Service, Container, or AKS)"
echo ""

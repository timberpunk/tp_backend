#!/bin/bash

# TimberPunk Backend - Production Startup Script
# Simple script to start backend with production settings

set -e

echo "🪵 Starting TimberPunk Backend"
echo "==============================="
echo ""

# Get script directory
cd "$(dirname "$0")"

# Check if .env exists
if [ ! -f ".env" ]; then
    echo "⚠️  Warning: .env file not found!"
    echo "Using default settings..."
fi

# Check if venv exists
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
fi

# Activate venv
echo "🐍 Activating virtual environment..."
source venv/bin/activate

# Install/Update dependencies
echo "📦 Installing dependencies..."
pip install --upgrade pip -q
pip install -r requirements.txt -q
pip install gunicorn -q

echo ""
echo "✅ Ready to start!"
echo ""

# Ask for mode
echo "Select mode:"
echo "1) Production (Gunicorn - recommended for VPS)"
echo "2) Development (Uvicorn - with auto-reload)"
read -p "Choice (1 or 2, default: 1): " MODE
MODE=${MODE:-1}

echo ""

if [ "$MODE" = "1" ]; then
    echo "🚀 Starting in PRODUCTION mode..."
    echo "📍 API: http://0.0.0.0:8000"
    echo "📚 Docs: http://0.0.0.0:8000/docs"
    echo ""
    echo "Press Ctrl+C to stop"
    echo ""
    gunicorn -c gunicorn.conf.py main:app
else
    echo "🔧 Starting in DEVELOPMENT mode..."
    echo "📍 API: http://127.0.0.1:8000"
    echo "📚 Docs: http://127.0.0.1:8000/docs"
    echo ""
    echo "Press Ctrl+C to stop"
    echo ""
    uvicorn main:app --host 0.0.0.0 --port 8000 --reload
fi

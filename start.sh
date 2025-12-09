#!/bin/bash

# TimberPunk Backend Startup Script

echo "🪵 Starting TimberPunk Backend..."
echo ""

# Check if PostgreSQL is running
if ! pg_isready > /dev/null 2>&1; then
    echo "⚠️  PostgreSQL is not running!"
    echo "Starting PostgreSQL..."
    if command -v brew &> /dev/null; then
        brew services start postgresql
    else
        sudo service postgresql start
    fi
    sleep 2
fi

# Check if database exists
if ! psql -lqt | cut -d \| -f 1 | grep -qw timberpunk; then
    echo "📊 Creating database 'timberpunk'..."
    createdb timberpunk
fi

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "🐍 Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "🐍 Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "📦 Installing dependencies..."
pip install -q -r requirements.txt

# Start the server
echo ""
echo "✅ Starting FastAPI server..."
echo "📝 API Documentation: http://localhost:8000/docs"
echo ""
uvicorn main:app --reload

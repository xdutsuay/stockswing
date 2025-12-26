#!/bin/bash

echo "🚀 Starting StockSwing..."

# Check requirements
if ! command -v python3 &> /dev/null; then
    echo "Error: python3 is not installed."
    exit 1
fi

if ! command -v npm &> /dev/null; then
    echo "Error: npm is not installed."
    exit 1
fi

# Start Backend
echo "Starting Backend..."
cd backend
# Check if venv exists
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi
source venv/bin/activate
echo "Ensuring dependencies..."
pip install fastapi[all] tensorflow pandas numpy pydantic-settings sqlmodel yfinance scikit-learn

# Run in background
uvicorn app.main:app --reload --port 8000 &
BACKEND_PID=$!
cd ..

# Start Frontend
echo "Starting Frontend..."
cd frontend
npm run dev &
FRONTEND_PID=$!
cd ..

echo "✅ StockSwing is running!"
echo "Backend: http://localhost:8000/docs"
echo "Frontend: http://localhost:3000"
echo "Press CTRL+C to stop."

trap "kill $BACKEND_PID $FRONTEND_PID; exit" INT
wait

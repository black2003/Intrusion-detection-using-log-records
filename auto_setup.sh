#!/bin/bash
# Define Python 3.10 path (update this if needed)
# Check if Python 3.10 exists
if [ ! -f "$PYTHON310" ]; then
  echo "❌ Python 3.10 not found at: $PYTHON310"
  echo "Please install Python 3.10.11 from https://www.python.org/downloads/release/python-31011/"
fi
echo "✅ Found Python 3.10 at: $PYTHON310"
"$PYTHON310" -m venv venv
# Activate the virtual environment
echo "⚙️ Activating virtual environment..."
# Upgrade pip, setuptools
pip install --upgrade pip setuptools
# Install requirements
echo "📦 Installing from requirements.txt..."
# Run the application
python app.py &

# Wait for the server to start

# Open the browser (works on most systems)
if command -v xdg-open >/dev/null 2>&1; then
  xdg-open http://127.0.0.1:5000/
elif command -v open >/dev/null 2>&1; then
  start http://127.0.0.1:5000/
else 
  echo "Please open http://127.0.0.1:5000/ in your browser"
echo "✅ Application is running at http://127.0.0.1:5000/"

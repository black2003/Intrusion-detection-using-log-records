#!/bin/bash
# Define Python 3.10 path (update this if needed)
PYTHON310="/c/Users/$(whoami)/AppData/Local/Programs/Python/Python310/python.exe"
# Check if Python 3.10 exists
if [ ! -f "$PYTHON310" ]; then
  echo "❌ Python 3.10 not found at: $PYTHON310"
  echo "Please install Python 3.10.11 from https://www.python.org/downloads/release/python-31011/"
  exit 1
fi
echo "✅ Found Python 3.10 at: $PYTHON310"
# Create virtual environment
echo "🔧 Creating virtual environment 'venv'..."
"$PYTHON310" -m venv venv
# Activate the virtual environment
echo "⚙️ Activating virtual environment..."
source venv/Scripts/activate
# Upgrade pip, setuptools
echo "⬆️ Upgrading pip and setuptools..."
pip install --upgrade pip setuptools
# Install requirements
echo "📦 Installing from requirements.txt..."
pip install -r requirements.txt
echo "✅ Setup complete. Your environment is ready and activated."

# Run the application
echo "🚀 Starting application..."
python app.py &

# Wait for the server to start
echo "⏳ Waiting for server to start..."
sleep 3

# Open the browser (works on most systems)
echo "🌐 Opening browser..."
if command -v xdg-open >/dev/null 2>&1; then
  xdg-open http://127.0.0.1:5000/
elif command -v open >/dev/null 2>&1; then
  open http://127.0.0.1:5000/
elif command -v start >/dev/null 2>&1; then
  start http://127.0.0.1:5000/
else 
  echo "Please open http://127.0.0.1:5000/ in your browser"
fi

echo "✅ Application is running at http://127.0.0.1:5000/"

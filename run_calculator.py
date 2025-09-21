#!/usr/bin/env python3
"""
ΛambdaCalc Enhanced Calculator Launcher
Simple script to start the enhanced calculator frontend with backend integration.
"""

import os
import sys
import subprocess
import webbrowser
import time
from pathlib import Path

def check_dependencies():
    """Check if required dependencies are installed."""
    try:
        import flask
        import flask_cors
        import numpy
        import sympy
        print("✅ All dependencies are installed")
        return True
    except ImportError as e:
        print(f"❌ Missing dependency: {e}")
        print("Please install dependencies with: pip install -r requirements.txt")
        return False

def start_server():
    """Start the Flask development server."""
    print("🧠📐 Starting ΛambdaCalc Enhanced Calculator...")
    print("=" * 60)
    print("🚀 Backend server starting on http://localhost:5000")
    print("🌐 Frontend will be available at the same URL")
    print("=" * 60)
    print("📱 Features:")
    print("   • Modern responsive design")
    print("   • Dark/Light theme toggle")
    print("   • Multiple calculator modes")
    print("   • Matrix operations")
    print("   • Calculus operations")
    print("   • Accessibility features")
    print("=" * 60)
    print("⌨️  Keyboard shortcuts:")
    print("   • Numbers: 0-9")
    print("   • Operators: +, -, *, /")
    print("   • Calculate: Enter or =")
    print("   • Clear: Escape or C")
    print("   • Backspace: Delete last digit")
    print("=" * 60)
    print("🛑 Press Ctrl+C to stop the server")
    print("=" * 60)
    
    # Wait a moment then open browser
    def open_browser():
        time.sleep(2)
        webbrowser.open('http://localhost:5000')
    
    import threading
    browser_thread = threading.Thread(target=open_browser)
    browser_thread.daemon = True
    browser_thread.start()
    
    # Start the Flask app
    try:
        from app import app
        app.run(debug=False, host='0.0.0.0', port=5000)
    except KeyboardInterrupt:
        print("\n👋 Calculator server stopped. Thank you for using ΛambdaCalc!")
    except Exception as e:
        print(f"❌ Error starting server: {e}")
        return False

def main():
    """Main function to launch the calculator."""
    print("🧠📐 ΛambdaCalc Enhanced Calculator Launcher")
    print("=" * 50)
    
    # Check if we're in the right directory
    if not Path('app.py').exists():
        print("❌ Error: app.py not found in current directory")
        print("Please run this script from the LambdaCalc project root")
        return
    
    # Check dependencies
    if not check_dependencies():
        return
    
    # Start the server
    start_server()

if __name__ == "__main__":
    main()

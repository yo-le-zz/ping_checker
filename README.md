Ping Checker

A simple Python script to test the reachability and response time of a website or IP address.

Created by: Yolezz (speaks French)

Features:
- Ping a custom IP address or domain.
- Show response time in milliseconds.
- Highlight reachable/unreachable hosts using colored console output.
- Works on Windows and Linux.

Requirements:
- Python 3.8+ to run the .py script
- Python library: colorama (for colored console output)

Install dependencies:
pip install -r requirements.txt

Usage (Python script):
python ping_checker.py

Executables:
- Windows: ping_checker.exe
- Linux: ping_checker (found in the 'dist/' folder)

Notes:
- macOS is not supported yet.
- To create a standalone executable you can use PyInstaller:

pyinstaller --onefile --hidden-import=colorama ping_checker.py

License:
This project is licensed under the MIT License.

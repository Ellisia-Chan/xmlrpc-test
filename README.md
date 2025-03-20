# xmlrpc-test

# Temperature Converter

A simple temperature converter GUI built with Python's `tkinter` and `xmlrpc` for remote conversion between Celsius and Fahrenheit.

## Features
- Connect to a remote XML-RPC server.
- Convert temperatures between Celsius and Fahrenheit.
- Real-time result display.

## Prerequisites
- Python 3.x

## Installation
1. Clone the repository:
```bash
git clone https://github.com/yourusername/temperature-converter.git
cd temperature-converter
```
2. Install required packages (if needed):
```bash
pip install tk
```

## Usage
1. Run the script:
```bash
python converter.py
```
2. Enter the server address and port.
3. Click **Connect** to establish a connection.
4. Choose the unit (Celsius or Fahrenheit), enter the value, and click **Convert**.
5. The result will be displayed below.

## XML-RPC Server Methods
Ensure the server implements these methods:
- `Celcius_to_Fahrenheit(value: float) -> float`
- `Fahrenheit_to_Celcius(value: float) -> float`

## Example Server (Python)
```python
from xmlrpc.server import SimpleXMLRPCServer

def Celcius_to_Fahrenheit(c):
    return (c * 9/5) + 32

def Fahrenheit_to_Celcius(f):
    return (f - 32) * 5/9

server = SimpleXMLRPCServer(("0.0.0.0", 8000))
server.register_function(Celcius_to_Fahrenheit, "Celcius_to_Fahrenheit")
server.register_function(Fahrenheit_to_Celcius, "Fahrenheit_to_Celcius")
print("Server running on port 8000...")
server.serve_forever()
```

## Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss the changes.

## License
[MIT](LICENSE)

---

Happy converting! 🌡️


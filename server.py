from xmlrpc.server import SimpleXMLRPCServer

server_ip = '14.0.4.201'
port = 6969

# This function runs the server.
def run_server():
    with SimpleXMLRPCServer((server_ip, port)) as server:
        # Register the Celcius_Fahrenheit_Converter class with the server.
        server.register_instance(Celcius_Fahrenheit_Converter())

        # Print a message to let the user know the server is running.
        print(f"Server running on {server_ip}:{port}")
        # Start the server.
        server.serve_forever()

# This class provides the Celcius_to_Fahrenheit and Fahrenheit_to_Celcius methods.
class Celcius_Fahrenheit_Converter:
    # This method takes a Celcius temperature and returns the equivalent Fahrenheit temperature.
    def Celcius_to_Fahrenheit(self, celsius):
        return (float(celsius) * 1.8) + 32
    
    # This method takes a Fahrenheit temperature and returns the equivalent Celcius temperature.
    def Fahrenheit_to_Celcius(self, fahrenheit):
        return (float(fahrenheit) - 32) / 1.8
    
if __name__ == "__main__":
    # Run the server.
    run_server()


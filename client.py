import tkinter as tk
from tkinter import ttk
import xmlrpc.client

# Define the server's address and port
server_address = ""  # Local IP of the server
server = None  # Server connection placeholder
connected_to_server = False


# Function to connect to the server
def connect_to_server():
    global server, server_address, connected_to_server
    ip = entry.get().strip()
    port = PORT_entry.get().strip()

    if ip and port:
        server_address = f"http://{ip}:{port}/"
        try:
            server = xmlrpc.client.ServerProxy(server_address)
            connected_to_server = True
            result_label.config(text=f"Connected to {server_address}", fg="green")
        except Exception as e:
            connected_to_server = False
            result_label.config(text=f"Connection failed: {e}", fg="red")
    else:
        connected_to_server = False
        result_label.config(text="Please enter a valid IP and Port", fg="red")


# Conversion function
def convert():
    global connected_to_server

    if not connected_to_server:
        result_label.config(text="Not connected to server", fg="red")
        return

    try:
        selected_unit = unit_var.get()  # Get the selected value from the combobox
        selected_unit_value = float(unit_val_entry.get())  # Combobox entry value

        # Perform conversion
        if selected_unit == "Celsius":
            result = server.Celcius_to_Fahrenheit(selected_unit_value)
        elif selected_unit == "Fahrenheit":
            result = server.Fahrenheit_to_Celcius(selected_unit_value)
        else:
            result_label.config(text="Invalid unit", fg="red")
            return

        # Update the result label
        result_label.config(text=f"Converted: {result:.2f}", fg="blue")

    except ValueError:
        result_label.config(text="Please enter a valid number", fg="red")
    except Exception as e:
        result_label.config(text=f"Conversion failed: {e}", fg="red")



# GUI Setup
root = tk.Tk()
root.title("Temperature Converter")
root.geometry("615x500")
root.resizable(False, False)
root.configure(bg="linen")  # Set background color

# Configure the grid to stretch the title label across the window width
root.grid_columnconfigure(0, weight=1)

# Title label (fits the full width)
lbl_title = tk.Label(root, bd=10, relief=tk.RIDGE, text="TEMPERATURE CONVERTER",
                     fg="blue", bg="linen", font=("Times New Roman", 25, "bold"))
lbl_title.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

# Frame (tk.Frame for bg support)
frame = tk.Frame(root, bg="linen", bd=10, relief=tk.RIDGE)
frame.grid(row=1, column=0, padx=10, pady=10, sticky=(tk.W, tk.E, tk.N, tk.S))

# Server Address
tk.Label(frame, text="Server Address:", bg="linen", font=("Arial", 14)).grid(row=0, column=0, padx=10, pady=10, sticky="w")
entry = ttk.Entry(frame, width=20, font=("Arial", 16))
entry.grid(row=0, column=1, padx=10, pady=10)

# Port Number
tk.Label(frame, text="Port:", bg="linen", font=("Arial", 14)).grid(row=1, column=0, padx=10, pady=10, sticky="w")
PORT_entry = ttk.Entry(frame, width=20, font=("Arial", 16))
PORT_entry.grid(row=1, column=1, padx=10, pady=10)

# Connect Button
connect_button = ttk.Button(frame, text="Connect", command=connect_to_server)
connect_button.grid(row=2, column=0, columnspan=2, pady=20)

# Unit Selection
tk.Label(frame, text="Unit:", bg="linen", font=("Arial", 14)).grid(row=3, column=0, padx=10, pady=10, sticky="w")
unit_var = tk.StringVar(value="Celsius")
unit_menu = ttk.Combobox(frame, textvariable=unit_var, values=["Celsius", "Fahrenheit"],
                         state="readonly", width=15, font=("Arial", 14))
unit_menu.grid(row=3, column=1, padx=10, pady=10)

# Value Entry
tk.Label(frame, text="Value:", bg="linen", font=("Arial", 14)).grid(row=4, column=0, padx=10, pady=10, sticky="w")
unit_val_entry = ttk.Entry(frame, width=20, font=("Arial", 16))
unit_val_entry.grid(row=4, column=1, padx=10, pady=10)

# Convert Button
convert_button = ttk.Button(frame, text="Convert", command=convert)
convert_button.grid(row=5, column=0, columnspan=2, pady=20)

# Result Label
result_label = tk.Label(frame, text="Not connected", font=("Arial", 16), bg="linen")
result_label.grid(row=6, column=0, columnspan=3, pady=10)

root.mainloop()

import serial.tools.list_ports

available_ports = [port.device for port in serial.tools.list_ports.comports()]
print("Available Ports:", available_ports)

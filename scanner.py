"""
This is a port scanner.
"""

import socket

# Define the target host and the ports you want to scan
target_host = "localhost" #replace with what you want
target_ports = [80, 443, 8080, 3306, 8783, 7070] #replace with what you want

# Define a function to scan a port and return whether it's open or not
def scan_port(host, port):
    # Create a socket object
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Set the timeout to 1 second to avoid hanging
    sock.settimeout(1)
    try:
        # Connect to the target host and port
        sock.connect((host, port))
        # If the connection was successful, the port is open
        print(f"Port {port} is open")
        return True
    except:
        # If the connection failed, the port is closed
        print(f"Port {port} is closed")
        return False
    finally:
        # Close the socket
        sock.close()

# Loop through the target ports and scan each one
for port in target_ports:
    scan_port(target_host, port)

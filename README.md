# pyPortScanners
Description: This repository is combined with a regular port scanner in python and then a Multi-threading port scanner in python as well.

# Regular port scanner:
This code will print whether each port in `target_ports` is open or closed. If the port is open, it will return `True`, otherwise it will return `False`. Note that scanning ports without permission is illegal in some countries and on some networks, so be sure to get permission before using this code.

# installing program requirements:
``pip3 install sockets socks requests``
- this is just in case...

# Usage:
``python3 scanner.py``

# ---------------------------------------------

# Multithreaded port scanner:
This code creates a separate thread for each port in `target_ports`, allowing the ports to be scanned in parallel. The `scan_port` function is the same as the single-threaded version, but is called by each thread. The `threads` list is used to keep track of all the threads, and the `join` method is called on each thread to wait for it to finish before the program exits. This code should be faster than the single-threaded version, especially when scanning a large number of ports.

# installing program requirements:
``pip3 install sockets socks requests threading``

# Usage:
``python3 multithreadedscan.py``

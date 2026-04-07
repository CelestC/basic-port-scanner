import socket

target = input("Enter the target IP address: ")

print(f"Scanning {target}...\n")

for port in range(1, 1025):  # scans ports 1 to 1024
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)

    result = s.connect_ex((target, port))
    
    if result == 0:
        print(f"Port {port} is open ✅")
    
    s.close()

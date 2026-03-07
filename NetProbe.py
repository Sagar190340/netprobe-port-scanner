import socket

print("=================================")
print(" NetProbe - Simple Port Scanner")
print(" Author: Sagar Dhar")
print("=================================")

target = input("Enter target IP: ")

ports = [21,22,23,25,53,80,110,139,143,443,445,3389]

print(f"\nScanning target {target}...\n")

for port in ports:

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)

    result = s.connect_ex((target, port))

    if result == 0:
        print(f"Port {port} OPEN")

    s.close()

print("\nScan complete.")
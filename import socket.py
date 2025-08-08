import subprocess

def capture_wireless_networks(interface='wlan0'):
    try:
        # Run the 'iwlist' command to scan for wireless networks
        result = subprocess.check_output(['sudo', 'iwlist', interface, 'scan'], text=True)
        networks = []
        for line in result.split('\n'):
            line = line.strip()
            if line.startswith('ESSID:'):
                essid = line.split(':')[1].strip('"')
                networks.append(essid)
        return networks
    except Exception as e:
        print(f"Error: {e}")
        return []

if __name__ == "__main__":
    interface = 'wlan0'  # Change this to your wireless interface
    networks = capture_wireless_networks(interface)
    print("Available Wireless Networks:")
    for net in networks:
        print(net)

import socket
import threading

def scan_port(ip, port, results):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            results.append(port)
        sock.close()
    except Exception:
        pass

def scan_ports(ip, start_port, end_port):
    threads = []
    open_ports = []
    for port in range(start_port, end_port + 1):
        t = threading.Thread(target=scan_port, args=(ip, port, open_ports))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    return open_ports

if __name__ == "__main__":
    target_ip = input("Enter target IP address: ")
    start_port = int(input("Enter start port: "))
    end_port = int(input("Enter end port: "))
    print(f"Scanning {target_ip} from port {start_port} to {end_port}...")
    open_ports = scan_ports(target_ip, start_port, end_port)
    if open_ports:
        print("Open ports:")
        for port in open_ports:
            print(f"Port {port} is open")
    else:
        print("No open ports found.")
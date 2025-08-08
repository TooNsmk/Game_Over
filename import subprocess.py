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
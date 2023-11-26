import time
import requests
import socket

def get_public_ipv4():
    try:
        response = requests.get("https://api64.ipify.org?format=json")
        if response.status_code == 200:
            data = response.json()
            return data.get("ip")
        else:
            return None
    except requests.RequestException as e:
        print("Failed to retrieve public IPv4 address:", e)
        return None

def get_public_ipv6():
    try:
        response = requests.get("https://api6.ipify.org?format.json")
        if response.status_code == 200:
            data = response.json()
            return data.get("ip")
        else:
            return None
    except requests.RequestException as e:
        print("Failed to retrieve public IPv6 address:", e)
        return None

def get_internal_ipv4():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.settimeout(0.1)
        s.connect(("8.8.8.8", 80))
        internal_ipv4 = s.getsockname()[0]
        s.close()
        return internal_ipv4
    except socket.error as e:
        print("Failed to retrieve internal IPv4 address:", e)
        return None

def get_internal_ipv6():
    try:
        s = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
        s.settimeout(0.1)
        s.connect(("2001:4860:4860::8888", 80))
        internal_ipv6 = s.getsockname()[0]
        s.close()
        return internal_ipv6
    except socket.error as e:
        print("Failed to retrieve internal IPv6 address:", e)
        return None

def get_location_info(ip_address):
    try:
        response = requests.get(f"http://ip-api.com/json/{ip_address}")
        if response.status_code == 200:
            data = response.json()
            if data.get("status") == "success":
                return data
            else:
                return None
        else:
            return None
    except requests.RequestException as e:
        print("Failed to retrieve location information:", e)
        return None

def send_bark_notification(title, message):
    bark_url = "https://YOUR.DOMAIN.COM"  # Replace with your own Bark device key

    payload = {
        "title": title,
        "body": message
    }

    try:
        response = requests.post(bark_url, params=payload)
        if response.status_code == 200:
            print("Bark notification sent successfully!")
    except requests.RequestException as e:
        print("Failed to send Bark notification:", e)

def check_internet_connection():
    ipv4_address = get_public_ipv4()
    ipv6_address = get_public_ipv6()
    internal_ipv4 = get_internal_ipv4()
    internal_ipv6 = get_internal_ipv6()

    if ipv4_address:
        ipv4_message = f"Public IPv4 Address: {ipv4_address}\n"
    else:
        ipv4_message = "Unable to query public IPv4 address\n"

    if ipv6_address:
        ipv6_message = f"Public IPv6 Address: {ipv6_address}\n"
    else:
        ipv6_message = "Unable to query public IPv6 address\n"

    if internal_ipv4:
        internal_ipv4_message = f"Internal IPv4 Address: {internal_ipv4}\n"
    else:
        internal_ipv4_message = "Unable to query internal IPv4 address\n"

    if internal_ipv6:
        internal_ipv6_message = f"Internal IPv6 Address: {internal_ipv6}\n"
    else:
        internal_ipv6_message = "Internal IPv6 Address: Unable to query\n"

    if ipv4_address or ipv6_address:
        location_info = get_location_info(ipv4_address)  # Assuming using IPv4 address to retrieve location information
        if location_info:
            message = f"Your Lenovo laptop has started\n{ipv4_message}{ipv6_message}{internal_ipv4_message}{internal_ipv6_message}Location: {location_info['city']}, {location_info['regionName']}, {location_info['country']}"
        else:
            message = f"Your Lenovo laptop has started\n{ipv4_message}{ipv6_message}{internal_ipv4_message}{internal_ipv6_message}Unable to retrieve location information"
    else:
        message = "Your Lenovo laptop has started\nUnable to query IP addresses"

    send_bark_notification("Your Lenovo Laptop Has Started", message)

if __name__ == "__main__":
    check_internet_connection()

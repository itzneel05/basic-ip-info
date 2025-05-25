import requests
import json
import sys

def get_ip_info(ip):
    try:
        # Query ip-api.com
        response = requests.get(f"http://ip-api.com/json/{ip}")
        data = response.json()
        
        if data["status"] == "fail":
            print(f"[-] Error: Invalid IP {ip}")
            return None
        
        # Extract key info
        info = {
            "IP": data["query"],
            "Country": data.get("country", "Unknown"),
            "City": data.get("city", "Unknown"),
            "ISP": data.get("isp", "Unknown"),
            "Hostname": data.get("reverse", "Unknown")
        }
        
        # Display results
        print(f"[+] IP Info for {ip}:")
        for key, value in info.items():
            print(f"  {key}: {value}")
        
        return info
    
    except Exception as e:
        print(f"[-] Error: {e}")
        return None

def save_to_json(info, filename="ip_info.json"):
    if info:
        with open(filename, "w") as f:
            json.dump(info, f, indent=4)
        print(f"[+] Results saved to {filename}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 ip_info.py <IP>")
        print("Example: python3 ip_info.py 8.8.8.8")
        sys.exit(1)
    
    ip = sys.argv[1]
    info = get_ip_info(ip)
    save_to_json(info)

if __name__ == "__main__":
    main()
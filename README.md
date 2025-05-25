# IP Info Gatherer

A lightweight Python tool for **passive reconnaissance**, gathering public IP information (geolocation, ISP, hostname) using the [ip-api.com](http://ip-api.com) API. Designed for cybersecurity enthusiasts learning **Open-Source Intelligence (OSINT)** and penetration testing. Results are displayed in the console and saved to a JSON file for easy analysis.

## Features
- Retrieves IP details: country, city, ISP, hostname.
- Saves results to `ip_info.json`.
- Simple command-line interface.

## Prerequisites
- Linux (Ubuntu/Kali recommended)
- Python 3, `requests`
- Install dependencies:
  ```bash
  pip3 install requests
  
## Usage
Run the script with an IP address:
```bash
python3 ip_info.py <IP>
```
**Example**:
```bash
python3 ip_info.py 8.8.8.8
```

---

Built by [itzneel05](https://github.com/itzneel05) as part of a cybersecurity learning journey. Feedback and contributions welcome!

# NMVA Tool

## Overview

**NMVA Tool** (Network Mapping & Vulnerability Assessment Tool) is a Python-based utility designed to help you identify potential security risks within your local network. It leverages the power of [Nmap](https://nmap.org/) to perform comprehensive network scans, including port scanning, service identification, and vulnerability detection—all from a simple command-line interface.

---

## Features

- **Automatic Network Detection:**  
  Automatically detects your local IP address and subnet range—no manual configuration required.

- **Flexible Scanning Options:**  
  Choose from multiple scan types:
  - Scan all hosts for open ports
  - Scan active hosts for the first 1000 ports and identify running services
  - Full vulnerability scan on all open ports
  - Prioritized vulnerability scan on the first 1000 ports

- **User-Friendly Interface:**  
  Simple prompts guide you through the scanning process.

- **Clear Output:**  
  Results are displayed in a readable format for easy analysis.

---

## Requirements

- **Python 3.6+**
- **Nmap** (must be installed and accessible from your system's PATH)

### Python Libraries

- `subprocess`
- `socket`
- `ipaddress`

All required libraries are part of the Python standard library.

---

## Installation

1. **Clone this repository:**
   ```bash
   git clone <repository-url>
   cd NMVA_Tool
   ```

2. **Ensure Nmap is installed:**
   ```bash
   sudo apt update
   sudo apt install nmap
   ```

3. **Run the tool:**
   ```bash
   python3 main.py
   ```

---

## Usage

1. **Start the tool:**
   ```bash
   python3 main.py
   ```

2. **Follow the prompts:**
   - The tool will display your local IP and subnet.
   - Choose a scan option by entering the corresponding number.
   - View the scan results directly in your terminal.

3. **Repeat or exit:**
   - After each scan, you can choose to run another scan or exit the tool.

---

## File Structure

```
banner.py      # Displays the tool banner
main.py        # Main entry point and user interface
scanner.py     # Handles Nmap scanning logic
utility.py     # Utility functions for IP and subnet detection
README.md      # This documentation
```

---

## Ethical Notice

> **Use Responsibly:**  
> This tool is intended for educational and authorized security assessment purposes only.  
> **Unauthorized scanning of networks is illegal and unethical.**  
> You are solely responsible for your actions and any consequences arising from misuse.

---

## Credits

- **CFCS2R Internship Project**
- Developed as a learning and demonstration tool for network security assessment.

---

## License

This project is provided for educational purposes. Please review and comply with all applicable laws and regulations before use.
# NMVA Tool

NMVA Tool (Network Mapping & Vulnerability Assessment Tool) is a Python-based CLI utility for scanning local networks, identifying open ports, running services, and potential vulnerabilities using Nmap. It is designed for security assessment, learning, and demonstration purposes.

---

## Features

- **Automatic Network Detection**: Detects your local IP and subnet automatically.
- **Flexible Scanning**: Multiple scan types (open ports, service detection, vulnerability scan).
- **User-Friendly CLI**: Guided prompts for easy use.
- **Logging**: Configurable log level via environment variable (`LOG_LEVEL`).
- **Container Ready**: Run easily in Docker.

---

## Requirements

- Python 3.6+
- Nmap (must be installed and accessible in the container or host)

### Python Dependencies

All dependencies are listed in `requirements.txt` and can be installed with pip.

---

## Installation & Usage

### Local (Linux)

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd NMVA_Tool
   ```
2. **Install Nmap:**
   ```bash
   sudo apt update && sudo apt install nmap
   ```
3. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the tool:**
   ```bash
   python3 main.py
   ```

### Docker

1. **Build the Docker image:**
   ```bash
   docker build -t nmva_tool .
   ```
2. **Run the container:**
   ```bash
   docker run --rm -it --network host nmva_tool
   ```
   > **Note:** The `--network host` flag is recommended for network scanning tools.

3. **Set log level (optional):**
   ```bash
   docker run --rm -it --network host -e LOG_LEVEL=DEBUG nmva_tool
   ```

---

## File Structure

```
banner.py      # Displays the tool banner
main.py        # Main entry point and user interface
scanner.py     # Handles Nmap scanning logic
utility.py     # Utility functions for IP and subnet detection
requirements.txt # Python dependencies
Dockerfile     # Containerization instructions
README.md      # Documentation
```

---

## Configuration

- `LOG_LEVEL`: Set the logging level (e.g., INFO, DEBUG, WARNING, ERROR). Default is INFO.

---

## Ethical Notice

> **Use Responsibly:**
> This tool is intended for educational and authorized security assessment purposes only.
> **Unauthorized scanning of networks is illegal and unethical.**
> You are solely responsible for your actions and any consequences arising from misuse.

---

## License

MIT License. See [LICENSE](LICENSE) for details.

---

## Contact

For questions or support, please contact [your.email@example.com].
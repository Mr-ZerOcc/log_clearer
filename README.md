# Log Cleaner

A simple Python-based log cleaning tool for Linux systems.

⚠ **Warning:** This tool removes system log files.  
Use only on systems you own or have explicit permission to test.

---

## Features
- Clean old and rotated logs
- Safe log cleanup option
- Clear `journalctl` logs
- Optional critical log cleanup (auth / identity logs)

---

## Usage

Run the script with root privileges:

```bash
sudo python3 cleaner.py [options]
sudo python3 cleaner.py --help

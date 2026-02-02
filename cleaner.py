import subprocess
import argparse

def get_user_input():
    parser = argparse.ArgumentParser(description="Log Cleaner")

    parser.add_argument("-r", "--rubbish", action="store_true",
                        help="Remove old and rotated logs")

    parser.add_argument("-s", "--safe", action="store_true",
                        help="Safe cleaning")

    parser.add_argument("-j", "--journal", action="store_true",
                        help="Clear journalctl logs")

    parser.add_argument("-c", "--critical", action="store_true",
                        help="⚠ Clear auth / identity logs")

    return parser.parse_args()

print("Cleaner started!")

def rubbish():
    subprocess.run("truncate -s 0 /var/log/alternatives.log.1", shell=True)
    subprocess.run("truncate -s 0 /var/log/alternatives.log.2.gz", shell=True)
    subprocess.run("truncate -s 0 /var/log/boot.log.1", shell=True)
    subprocess.run("truncate -s 0 /var/log/boot.log.2", shell=True)
    subprocess.run("truncate -s 0 /var/log/boot.log.3", shell=True)
    subprocess.run("truncate -s 0 /var/log/dpkg.log.1", shell=True)
    subprocess.run("truncate -s 0 /var/log/dpkg.log.2.gz", shell=True)
    subprocess.run("truncate -s 0 /var/log/macchanger.log.1.gz", shell=True)
    subprocess.run("truncate -s 0 /var/log/macchanger.log.2.gz", shell=True)
    subprocess.run("truncate -s 0 /var/log/Xorg.0.log.old", shell=True)

def safe():
    subprocess.run("rm -f /var/log/*.gz", shell=True)
    subprocess.run("rm -f /var/log/*.1", shell=True)
    subprocess.run("rm -f /var/log/*.old", shell=True)
    subprocess.run("rm -f /var/log/macchanger.log*", shell=True)

def journal():
    subprocess.run("journalctl --disk-usage", shell=True)
    subprocess.run("journalctl --vacuum-time=7d", shell=True)

def critical():
    subprocess.run("truncate -s 0 /var/log/btmp", shell=True)
    subprocess.run("truncate -s 0 /var/log/wtmp", shell=True)
    subprocess.run("truncate -s 0 /var/log/lastlog", shell=True)

# -------- MAIN --------
args = get_user_input()

if args.rubbish:
    rubbish()

if args.safe:
    safe()

if args.journal:
    journal()

if args.critical:
    critical()

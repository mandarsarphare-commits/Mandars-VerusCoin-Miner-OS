import subprocess
import time
import os
from datetime import datetime

def miner_running():
    out = subprocess.run(
        ["screen", "-ls"],
        capture_output=True,
        text=True
    ).stdout
    return "miner" in out

while True:
    os.system("clear")
    print("=" * 60)
    print("   MANDAR'S VERUSCOIN MINER OS v1.0")
    print("=" * 60)
    print()

    print("Time :", datetime.now().strftime("%H:%M:%S"))

    if miner_running():
        print("Miner : 🟢 RUNNING")
    else:
        print("Miner : 🔴 STOPPED")

    uptime = subprocess.getoutput("uptime")
    print()
    print("System :", uptime)

    print()
    print("--------------------------------------------")
    print("Version : v1.0")
    print("Developer : Mandar")
    print("Dashboard refreshes every 2 seconds")
    time.sleep(2)

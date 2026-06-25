import subprocess
import json
from datetime import datetime

with open("config.json") as f:
    cfg = json.load(f)

result = subprocess.run(
    ["screen", "-ls"],
    capture_output=True,
    text=True
)

running = "miner" in result.stdout

print("=" * 60)
print("      MANDAR'S VERUSCOIN  MINER OS")
print("=" * 60)

print("Time      :", datetime.now().strftime("%H:%M:%S"))
print("Status    :", "🟢 Running" if running else "🔴 Stopped")
print("Threads   :", cfg["threads"])
print("Algorithm :", cfg["algorithm"])
print("Wallet    :", cfg["wallet"][:8] + "..." + cfg["wallet"][-6:])
print("=" * 40)

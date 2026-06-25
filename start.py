import json
import subprocess

with open("config.json", "r") as f:
    cfg = json.load(f)

cmd = [
    "screen",
    "-dmS",
    "miner",
    "/data/data/com.termux/files/home/ccminer/ccminer",
    "-a", cfg["algorithm"],
    "-o", cfg["pool"],
    "-u", cfg["wallet"],
    "-p", cfg["password"],
    "-t", str(cfg["threads"])
]

subprocess.run(cmd)
print(f"✅ Miner started with {cfg['threads']} thread(s)")

import subprocess

subprocess.run(["screen", "-S", "miner", "-X", "quit"])
print("🛑 Miner stopped")

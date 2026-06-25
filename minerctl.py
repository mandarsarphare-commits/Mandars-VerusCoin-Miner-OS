import subprocess

def status():
    result = subprocess.run(
        ["screen", "-ls"],
        capture_output=True,
        text=True
    )

    if "miner" in result.stdout:
        print("✅ Miner is running")
    else:
        print("❌ Miner is stopped")

if __name__ == "__main__":
    status()


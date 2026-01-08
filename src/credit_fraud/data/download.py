import subprocess
from pathlib import Path
import zipfile

DATA_DIR = Path("data/raw")
CSV_PATH = DATA_DIR / "creditcard.csv"
DATASET = "mlg-ulb/creditcardfraud"

def main():
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    if CSV_PATH.exists():
        print(f"✅ Found {CSV_PATH}")
        return

    print("⬇️ Downloading dataset from Kaggle...")
    # This will download a zip (often named creditcard.csv.zip)
    subprocess.check_call([
        "kaggle", "datasets", "download",
        "-d", DATASET,
        "-p", str(DATA_DIR),
        "-f", "creditcard.csv",
        "--force",
    ])

    # Find any zip produced by kaggle in that folder
    zip_files = sorted(DATA_DIR.glob("*.zip"), key=lambda p: p.stat().st_mtime, reverse=True)
    if not zip_files:
        raise FileNotFoundError(f"No .zip found in {DATA_DIR} after Kaggle download")

    zip_path = zip_files[0]
    print(f"📦 Unzipping {zip_path.name} ...")

    with zipfile.ZipFile(zip_path, "r") as zf:
        zf.extractall(DATA_DIR)

    if not CSV_PATH.exists():
        # Kaggle sometimes stores with different casing/name; try to locate it
        candidates = list(DATA_DIR.glob("**/*.csv"))
        raise FileNotFoundError(
            f"Expected {CSV_PATH} after unzip. Found CSVs: {[c.name for c in candidates]}"
        )

    print(f"✅ Ready: {CSV_PATH}")
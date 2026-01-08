import pandas as pd
from pathlib import Path

RAW_DIR = Path("data/raw")
PARQUET_PATH = RAW_DIR / "transactions_canonical.parquet"
CSV_PATH = RAW_DIR / "creditcard.csv"

def main():
    if PARQUET_PATH.exists():
        print(f"✅ Found {PARQUET_PATH}")
        return

    print("📄 Reading CSV...")
    df = pd.read_csv(CSV_PATH)

    # basic schema sanity
    required = {"Time", "Amount", "Class"}
    if not required.issubset(df.columns):
        raise ValueError(f"Missing columns: {required - set(df.columns)}")

    print("💾 Writing Parquet...")
    df.to_parquet(PARQUET_PATH, index=False)

    print("🧹 Cleaning up raw files...")
    CSV_PATH.unlink(missing_ok=True)
    for zip_file in RAW_DIR.glob("*.zip"):
        zip_file.unlink()

    print(f"✅ Ready: {PARQUET_PATH}")
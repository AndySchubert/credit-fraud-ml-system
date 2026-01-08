import os
import pandas as pd
from xgboost import XGBClassifier

# Kernel-safe settings
os.environ["OMP_NUM_THREADS"] = "1"
os.environ["MKL_NUM_THREADS"] = "1"


def main():
    X_train = pd.read_parquet("data/processed/X_train.parquet")
    X_test = pd.read_parquet("data/processed/X_test.parquet")
    y_train = pd.read_parquet("data/processed/y_train.parquet").squeeze()
    y_test = pd.read_parquet("data/processed/y_test.parquet").squeeze()

    # Safety
    if "transaction_time" in X_train.columns:
        X_train = X_train.drop(columns=["transaction_time"])
        X_test = X_test.drop(columns=["transaction_time"])

    scale_pos_weight = (y_train == 0).sum() / max((y_train == 1).sum(), 1)

    model = XGBClassifier(
        n_estimators=200,
        max_depth=4,
        learning_rate=0.05,
        subsample=0.8,
        colsample_bytree=0.8,
        scale_pos_weight=scale_pos_weight,
        eval_metric="logloss",
        tree_method="hist",
        n_jobs=1,
        random_state=42,
    )

    model.fit(X_train, y_train)

    os.makedirs("models", exist_ok=True)
    model.get_booster().save_model("models/xgb_fraud.json")

    print("✅ Model trained and saved to models/xgb_fraud.json")


if __name__ == "__main__":
    main()

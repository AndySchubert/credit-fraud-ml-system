# Feature Categories & Rationale

This document defines the main categories of features for the credit fraud ML system.

## 1. Transaction-Level Features
- Amount
- Merchant category
- Time of day
- Transaction type (online, POS, ATM)
- Device/browser info
**Rationale:** Immediate characteristics of each transaction. Helps detect anomalies.

## 2. Customer-Level Features
- Average transaction amount per day/week
- Transaction frequency
- Account age
- Recent unusual activity
**Rationale:** Detect deviations from typical behavior for individual customers.

## 3. Location & Velocity Features
- Geolocation of transaction vs usual location
- Distance between consecutive transactions
- Number of transactions within last X minutes
**Rationale:** Rapid, geographically inconsistent transactions often indicate fraud.

## 4. Historical & Behavioral Features
- Past fraud flags
- Chargeback history
- Payment method history
- Recurring patterns
**Rationale:** Captures patterns over time; improves predictive power.

## 5. Derived / Engineered Features
- Transaction amount normalized by average
- Velocity score (transactions per hour)
- Device risk score
**Rationale:** Combine raw features into meaningful indicators for the model.

## Notes
- These features will be engineered in `features/` folder.
- Each category will later map to pipelines for preprocessing and model input.
- Feature importance and explainability will be tracked via SHAP.

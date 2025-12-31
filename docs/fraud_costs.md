# Fraud vs Manual Review Cost Assumptions

## Overview
In real-world credit card transaction systems, every decision has a cost:

1. **False Negative (FN)** – fraudulent transaction is approved
   - Cost: financial loss due to fraud
   - Example: $100 lost per fraudulent transaction
2. **False Positive (FP)** – legitimate transaction is flagged for review
   - Cost: operational cost and customer inconvenience
   - Example: $5 per manual review

## Assumptions for Modeling
| Decision | Description                     | Cost per Event |
|----------|---------------------------------|----------------|
| FN       | Fraud transaction approved      | $100           |
| FP       | Legitimate transaction flagged  | $5             |
| TP       | Fraud detected                  | $0             |
| TN       | Legitimate transaction approved | $0             |

## Notes
- Costs are **simplified and illustrative**; actual costs vary by institution.
- The model will optimize **total expected cost**, not just accuracy.
- These assumptions will guide:
  - Threshold selection for fraud risk score
  - Feature engineering and alert prioritization
  - Evaluation metrics (cost-sensitive PR curve)
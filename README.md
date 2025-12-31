# Credit Fraud Risk Scoring System

## Overview
This project implements a production-style credit card transaction fraud detection system.
The goal is to score transactions in real time under realistic constraints such as class
imbalance, latency requirements, cost-sensitive decisions, and regulatory explainability.

This is not a Kaggle-style model-only project, but an end-to-end risk scoring system design.

## Problem Statement
Financial institutions must detect fraudulent card transactions while minimizing false
positives that negatively impact customer experience and increase manual review costs.

The system assigns a fraud risk score to each transaction and outputs an action:
- Approve
- Send to manual review
- Block

## Key Concepts
- Time-aware feature engineering
- Cost-based model evaluation
- Explainable predictions
- Real-time inference API
- Monitoring for data and prediction drift

## Status
Initial project scaffolding.

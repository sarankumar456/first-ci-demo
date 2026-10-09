def predict_churn(tenure, monthly_charges, contract):
    """Return a demonstration churn label using simple rules.

    This is an educational rule-based example, not a trained ML model.
    """
    if tenure < 0 or monthly_charges < 0:
        raise ValueError("Tenure and monthly charges must be non-negative.")

    if contract not in ("Month-to-month", "One year", "Two year"):
        raise ValueError("Unsupported contract type.")

    if contract == "Month-to-month" and tenure < 12 and monthly_charges >= 80:
        return "CHURN"

    return "NO_CHURN"


if __name__ == "__main__":
    customer = {
        "tenure": 6,
        "monthly_charges": 95.0,
        "contract": "Month-to-month"
    }

    print("Predicted customer status:", predict_churn(**customer))

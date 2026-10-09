import unittest

from telecom_logic import predict_churn


class TestTelecomLogic(unittest.TestCase):

    def test_high_risk_customer(self):
        result = predict_churn(
            tenure=6,
            monthly_charges=95.0,
            contract="Month-to-month"
        )
        self.assertEqual(result, "CHURN")

    def test_long_term_customer(self):
        result = predict_churn(
            tenure=36,
            monthly_charges=70.0,
            contract="Two year"
        )
        self.assertEqual(result, "NO_CHURN")

    def test_negative_tenure_raises_error(self):
        with self.assertRaises(ValueError):
            predict_churn(
                tenure=-1,
                monthly_charges=70.0,
                contract="One year"
            )

    def test_invalid_contract_raises_error(self):
        with self.assertRaises(ValueError):
            predict_churn(
                tenure=12,
                monthly_charges=70.0,
                contract="Monthly forever"
            )


if __name__ == "__main__":
    unittest.main()

# test_data_bill.py

import unittest
from unittest.mock import patch
from io import StringIO
import runpy


class TestDataBill(unittest.TestCase):

    def run_program(self, inputs):
        """
        Runs the full data_bill.py file using fake user inputs.
        Returns everything printed by the program.
        """
        with patch("builtins.input", side_effect=inputs):
            with patch("sys.stdout", new_callable=StringIO) as fake_output:
                runpy.run_path("data_bill.py")
                return fake_output.getvalue()

    def test_within_limit_regular_user(self):
        output = self.run_program(["8", "40", "no"])

        self.assertIn("You are within your data limit.", output)
        self.assertIn("GB over limit: 0", output)
        self.assertIn("Overage cost: $0.00", output)
        self.assertIn("Total bill: $40.00", output)

    def test_exactly_10_gb_premium_user(self):
        output = self.run_program(["10", "35", "yes"])

        self.assertIn("You are within your data limit.", output)
        self.assertIn("GB over limit: 0", output)
        self.assertIn("Overage cost: $0.00", output)
        self.assertIn("Total bill: $35.00", output)

    def test_tier_2_regular_user(self):
        output = self.run_program(["15", "50", "no"])

        self.assertIn("You are 5.0 GB over your limit.", output)
        self.assertIn("Overage rate: $2 per GB", output)
        self.assertIn("Overage cost: $10.00", output)
        self.assertIn("Total bill: $60.00", output)

    def test_tier_2_premium_user(self):
        output = self.run_program(["15", "50", "yes"])

        self.assertIn("You are 5.0 GB over your limit.", output)
        self.assertIn("Overage rate: $1 per GB", output)
        self.assertIn("Overage cost: $5.00", output)
        self.assertIn("Total bill: $55.00", output)

    def test_exactly_20_gb_regular_user(self):
        output = self.run_program(["20", "45", "no"])

        self.assertIn("You are 10.0 GB over your limit.", output)
        self.assertIn("Overage rate: $2 per GB", output)
        self.assertIn("Overage cost: $20.00", output)
        self.assertIn("Total bill: $65.00", output)

    def test_exactly_20_gb_premium_user(self):
        output = self.run_program(["20", "45", "yes"])

        self.assertIn("You are 10.0 GB over your limit.", output)
        self.assertIn("Overage rate: $1 per GB", output)
        self.assertIn("Overage cost: $10.00", output)
        self.assertIn("Total bill: $55.00", output)

    def test_tier_3_regular_user(self):
        output = self.run_program(["25", "40", "no"])

        self.assertIn("You are 15.0 GB over your limit.", output)
        self.assertIn("Overage rate: $3 per GB", output)
        self.assertIn("Overage cost: $45.00", output)
        self.assertIn("Total bill: $85.00", output)

    def test_tier_3_premium_user(self):
        output = self.run_program(["25", "40", "yes"])

        self.assertIn("You are 15.0 GB over your limit.", output)
        self.assertIn("Overage rate: $2 per GB", output)
        self.assertIn("Overage cost: $30.00", output)
        self.assertIn("Total bill: $70.00", output)

    def test_decimal_tier_2_regular_user(self):
        output = self.run_program(["10.5", "40", "no"])

        self.assertIn("You are 0.5 GB over your limit.", output)
        self.assertIn("Overage rate: $2 per GB", output)
        self.assertIn("Overage cost: $1.00", output)
        self.assertIn("Total bill: $41.00", output)

    def test_decimal_tier_3_regular_user(self):
        output = self.run_program(["20.1", "40", "no"])

        self.assertIn("You are 10.1 GB over your limit.", output)
        self.assertIn("Overage rate: $3 per GB", output)
        self.assertIn("Overage cost: $30.30", output)
        self.assertIn("Total bill: $70.30", output)


if __name__ == "__main__":
    unittest.main()
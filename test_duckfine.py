import unittest

from duckfine import DuckFine


class TestDuckFine(unittest.TestCase):
    def test_stores_member_id(self):
        fine = DuckFine("member-123")
        self.assertEqual(fine.member_id, "member-123")

    def test_starts_with_no_amount_owed(self):
        fine = DuckFine("member-123")
        self.assertEqual(fine.total_owed, 0.0)

    def test_forgives_first_two_days_late(self):
        fine = DuckFine("member-123")
        self.assertEqual(fine.charge(2), 0.0)

    def test_charges_standard_rate_after_grace_period(self):
        fine = DuckFine("member-123")
        self.assertEqual(fine.charge(4), 1.0)

    def test_charges_double_rate_for_deluxe_fine(self):
        fine = DuckFine("member-123")
        self.assertEqual(fine.charge(4, deluxe=True), 2.0)

    def test_caps_a_single_charge_at_maximum_fee(self):
        fine = DuckFine("member-123")
        self.assertEqual(fine.charge(20), 5.0)

    def test_adds_each_charge_to_total_owed(self):
        fine = DuckFine("member-123")

        fine.charge(4)
        fine.charge(3)

        self.assertEqual(fine.total_owed, 1.5)

    def test_rejects_negative_days_late(self):
        fine = DuckFine("member-123")

        with self.assertRaises(ValueError):
            fine.charge(-1)


if __name__ == "__main__": # pragma: no cover 
    unittest.main()
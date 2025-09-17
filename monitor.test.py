import unittest
from monitor import vitals_ok, is_temperature_ok, is_pulse_ok, is_spo2_ok

class TestVitalsFunctions(unittest.TestCase):

    def test_temperature_ok(self):
        self.assertTrue(is_temperature_ok(98.6))
        self.assertFalse(is_temperature_ok(103))
        self.assertFalse(is_temperature_ok(94))

    def test_pulse_ok(self):
        self.assertTrue(is_pulse_ok(75))
        self.assertFalse(is_pulse_ok(55))
        self.assertFalse(is_pulse_ok(105))

    def test_spo2_ok(self):
        self.assertTrue(is_spo2_ok(95))
        self.assertFalse(is_spo2_ok(89))

    def test_vitals_ok_all_good(self):
        self.assertTrue(vitals_ok(98.6, 75, 95))

    def test_vitals_ok_bad_temperature(self):
        self.assertFalse(vitals_ok(103, 75, 95))

    def test_vitals_ok_bad_pulse(self):
        self.assertFalse(vitals_ok(98.6, 55, 95))

    def test_vitals_ok_bad_spo2(self):
        self.assertFalse(vitals_ok(98.6, 75, 89))

    def test_vitals_ok_multiple_bad(self):
        self.assertFalse(vitals_ok(103, 105, 85))

if __name__ == '__main__':
    unittest.main()

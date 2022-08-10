from calc import SimpleCalc
import pytest
import unittest

class Caltests(unittest.TestCase):
    calc_obj = SimpleCalc()

    def test_add(self):
        self.assertEqual(self.calc_obj.add(2,4), 6)

    def test_subtract(self):
        self.assertEqual(self.calc_obj.subtract(4,2), 2)

    def test_multiply(self):
        self.assertEqual(self.calc_obj.multiply(2,2), 4)

    def test_divide(self):
        self.assertEqual(self.calc_obj.divide(4,2), 2)

    def test_conversion_cm_to_mtr(self):
        self.assertEqual(self.calc_obj.conversion_cm_to_mtr(100), 1)

    def test_percentage(self):
        self.assertEqual(self.calc_obj.percentage(50,100), 50)

    def test_DOB(self):
        self.assertEqual(self.calc_obj.DOB(1995,4),"Your DOB is 1995 / 4")

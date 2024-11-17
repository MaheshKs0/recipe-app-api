"""sample tests"""

from django.test import SimpleTestCase
from app.calc import add, subtract

class CalculatorTest(SimpleTestCase):
    def test_addition(self):
        res = add(1,2)
        self.assertEquals(res,3)

    def test_subtract(self):
        res = subtract(12,6)
        self.assertEquals(res,6)
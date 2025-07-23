"""
Sample test file for the app.
"""

from django.test import SimpleTestCase

from . import calc

class CalcTests(SimpleTestCase):
    """Test the calc module."""
    
    def test_add_numbers(self):
        """Test adding two numbers together."""
        result = calc.add(3, 8)
        self.assertEqual(result, 11)
    
    def test_subtract_numbers(self):
        """Test subtracting two numbers."""
        result = calc.subtract(10, 5)
        self.assertEqual(result, 5)

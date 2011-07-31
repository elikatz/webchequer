from django.core.exceptions import ValidationError
from scheduler import validateDayOfWeek
import unittest

class ValidationTest(unittest.TestCase):
    def test_validate_day_of_the_week(self):
        self.assertRaises(ValidationError, validateDayOfWeek,('MWT'))
        self.assertRaises(ValidationError, validateDayOfWeek,('MG'))
        self.assertRaises(ValidationError, validateDayOfWeek,('MMT'))
        self.assertRaises(ValidationError, validateDayOfWeek,('SS'))
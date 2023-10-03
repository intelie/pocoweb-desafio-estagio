from django.test import TestCase
from explorer.models import Oilfield, OperationalUnit, Well

from explorer.services import process_data_challenge1, process_data_challenge2

class Challenge1TestCase(TestCase):
    # def setUp(self):
        # .....

    def should_test_something(self):
        """Describe the test"""
        opunits = OperationalUnit.objects.all()
        oilfields = Oilfield.objects.all()
        wells = Well.objects.all()
        result = []
        
        self.assertEqual(process_data_challenge1(opunits, oilfields, wells), result)

class Challenge2TestCase(TestCase):
    # def setUp(self):
        # ....

    def should_test_something(self):
        """Describe the test"""
        opunits = OperationalUnit.objects.all()
        oilfields = Oilfield.objects.all()
        wells = Well.objects.all()
        result = []
        
        self.assertEqual(process_data_challenge2(opunits, oilfields, wells), result)
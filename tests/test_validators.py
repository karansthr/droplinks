import sys
import unittest
sys.path.append("..")

from core import validators
from core.services import Service

class TestValidors(unittest.TestCase):
    
    def setUp(self):
        class TestClass(Service):
            name = validators.String(min_length=2)
            email = validators.Email(max_length=120)
            address = validators.String(min_length=5, max_length=30)
            is_admin = validators.Boolean()
        
        self.TestClass = TestClass
    
    def test_email(self):
        t = self.TestClass({'email': 'karansthr97@gmail.com'}, strict=False)
        self.assertTrue(t.is_valid())
        t = self.TestClass({'email': 'karansthr97gmail.com'}, strict=False)
        self.assertFalse(t.is_valid())

    def test_boolean(self):
        t = self.TestClass({'is_admin': True}, strict=False)
        self.assertTrue(t.is_valid())

    def test_string(self):
        t = self.TestClass({'address': '127 Baker Street'}, strict=False)
        self.assertTrue(t.is_valid())
        t = self.TestClass({'address': '127'}, strict=False) # < 5
        self.assertFalse(t.is_valid())
        t = self.TestClass(
            {'address': '127 Baker Street127 Baker Street127 Baker Street'},
            strict=False
            ) # > 30
        self.assertFalse(t.is_valid())

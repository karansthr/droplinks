import sys
import unittest

sys.path.append("..")

from core import validators
from core.services import Service


class TestClass(Service):
    name = validators.String(min_length=2)
    email = validators.Email(max_length=120)
    address = validators.String(min_length=5, max_length=30)
    is_admin = validators.Boolean()


class TestValidors(unittest.TestCase):

    # def test_email(self):
    #     t = TestClass({'email': 'karansthr97@gmail.com'}, strict=False)
    #     self.assertTrue(t.is_valid())
    #     t = TestClass({'email': 'karansthr97gmail.com'}, strict=False)
    #     self.assertFalse(t.is_valid())

    # def test_boolean(self):
    #     t = TestClass({'is_admin': True}, strict=False)
    #     self.assertTrue(t.is_valid())

    def test_string(self):
        t = TestClass({"name": "k"})
        self.assertFalse(t.is_valid())
        # t = TestClass({'address': '127 Baker Stret'}, strict=False)
        # self.assertTrue(t.is_valid())
        # t = TestClass({'address': '127'}, strict=False) # < 5
        # self.assertFalse(t.is_valid())
        # t = TestClass(
        #     {'address': '127 Baker Street127 Baker Street127 Baker Street'},
        #     strict=False
        #     ) # > 30
        # self.assertFalse(t.is_valid())

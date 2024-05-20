import unittest

from superdirtpy.params import Params


class TestSuperDirtParams(unittest.TestCase):
    def test_superdirt_params(self):
        self.assertEqual(Params.s, "s")

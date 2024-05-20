import unittest

from superdirtpy.scales import Scales


class TestScales(unittest.TestCase):
    def test_scales(self):
        self.assertEqual(Scales.min_pent, [0, 3, 5, 7, 10])

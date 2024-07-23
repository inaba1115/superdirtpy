import unittest

from superdirtpy.utils import zmap


class TestUtils(unittest.TestCase):
    def test_zmap(self):
        self.assertAlmostEqual(zmap(5, 0, 10, 0, 100), 50.0)
        self.assertEqual(round(zmap(0.5, 0, 1, 0, 127)), 64)
        self.assertAlmostEqual(round(zmap(64, 0, 127, 0, 1), 1), 0.5)
        self.assertEqual(round(zmap(0, -1, 1, 0, 127)), 64)
        self.assertEqual(round(zmap(2, 0, 1, 0, 127)), 127)
        self.assertEqual(round(zmap(-2, 0, 1, 0, 127)), 0)

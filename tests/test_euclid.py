import unittest

from superdirtpy.euclid import euclid


class TestEuclid(unittest.TestCase):
    def test_euclid(self):
        self.assertEqual(euclid(2, 5), "x.x..")
        self.assertEqual(euclid(3, 4), "x.xx")
        self.assertEqual(euclid(3, 5), "x.x.x")
        self.assertEqual(euclid(3, 7), "x.x.x..")
        self.assertEqual(euclid(3, 8), "x..x..x.")
        self.assertEqual(euclid(4, 7), "x.x.x.x")
        self.assertEqual(euclid(4, 9), "x.x.x.x..")
        self.assertEqual(euclid(4, 11), "x..x..x..x.")
        self.assertEqual(euclid(5, 6), "x.xxxx")
        self.assertEqual(euclid(5, 7), "x.xx.xx")
        self.assertEqual(euclid(5, 8), "x.xx.xx.")
        self.assertEqual(euclid(5, 9), "x.x.x.x.x")
        self.assertEqual(euclid(5, 11), "x.x.x.x.x..")
        self.assertEqual(euclid(5, 12), "x..x.x..x.x.")
        self.assertEqual(euclid(5, 16), "x..x..x..x..x...")
        self.assertEqual(euclid(7, 8), "x.xxxxxx")
        self.assertEqual(euclid(7, 12), "x.xx.x.xx.x.")
        self.assertEqual(euclid(7, 16), "x..x.x.x..x.x.x.")
        self.assertEqual(euclid(9, 16), "x.xx.x.x.xx.x.x.")
        self.assertEqual(euclid(11, 24), "x..x.x.x.x.x..x.x.x.x.x.")
        self.assertEqual(euclid(13, 24), "x.xx.x.x.x.x.xx.x.x.x.x.")

    def test_euclid_rotate(self):
        self.assertEqual(euclid(2, 5, -1), ".x.x.")
        self.assertEqual(euclid(2, 5, 0), "x.x..")
        self.assertEqual(euclid(2, 5, 1), ".x..x")
        self.assertEqual(euclid(2, 5, 2), "x..x.")
        self.assertEqual(euclid(2, 5, 3), "..x.x")
        self.assertEqual(euclid(2, 5, 4), ".x.x.")
        self.assertEqual(euclid(2, 5, 5), "x.x..")
        self.assertEqual(euclid(2, 5, 6), ".x..x")

    def test_euclid_error(self):
        with self.assertRaises(ValueError):
            euclid(0, 0)

        self.assertEqual(euclid(0, 1), ".")
        self.assertEqual(euclid(1, 1), "x")

        with self.assertRaises(ValueError):
            euclid(2, 1)

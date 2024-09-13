import unittest

from superdirtpy.utils import bind_method, zmap


class TestUtils(unittest.TestCase):
    def test_zmap(self):
        self.assertAlmostEqual(zmap(5, 0, 10, 0, 100), 50.0)
        self.assertEqual(int(zmap(0.5, 0, 1, 0, 127)), 63)
        self.assertAlmostEqual(round(zmap(64, 0, 127, 0, 1), 1), 0.5)
        self.assertEqual(int(zmap(0, -1, 1, 0, 127)), 63)
        self.assertEqual(int(zmap(2, 0, 1, 0, 127)), 127)
        self.assertEqual(int(zmap(-2, 0, 1, 0, 127)), 0)

    def test_bind_method(self):
        self.assertEqual(
            bind_method([-1, 0, 1], [0, 1, 2], {0: 0, 1: None, 2: [0, 2, 4]}),
            [-1, None, [1, 3, 5]],
        )
        self.assertEqual(bind_method([0, 1, 2], [0], {0: 0}), [0, 1, 2])
        self.assertEqual(bind_method([0, 1, 2], [0], {}), [None, None, None])

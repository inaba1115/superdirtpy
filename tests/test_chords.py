import unittest

from superdirtpy.chords import Chords


class TestChords(unittest.TestCase):
    def test_chords(self):
        self.assertEqual(Chords.major, [0, 4, 7])

    def test_random(self):
        _, _ = Chords.random()
        _ = Chords.random(with_name=False)

import unittest

from superdirtpy.chords import Chords


class TestChords(unittest.TestCase):
    def test_chords(self):
        self.assertEqual(Chords.major, [0, 4, 7])

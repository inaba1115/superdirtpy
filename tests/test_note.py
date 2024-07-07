import unittest

from superdirtpy.note import Note, PitchClass


class TestPitchClass(unittest.TestCase):
    def test_random(self):
        _, _ = PitchClass.random()


class TestNote(unittest.TestCase):
    def test_init(self):
        note = Note(PitchClass.C, 5)
        self.assertEqual(note.midi_number, 60)

    def test_eq(self):
        note1 = Note(PitchClass.C, 5)
        note2 = Note(PitchClass.C, 5)
        note3 = Note(PitchClass.Cs, 5)
        self.assertTrue(note1 == note2)
        self.assertFalse(note1 != note2)
        self.assertTrue(note1 != note3)
        self.assertFalse(note1 == note3)

    def test_le(self):
        note1 = Note(PitchClass.C, 5)
        note2 = Note(PitchClass.C, 5)
        note3 = Note(PitchClass.Cs, 5)
        self.assertTrue(note1 < note3)
        self.assertTrue(note1 <= note2)
        self.assertFalse(note1 >= note3)
        self.assertFalse(note1 > note2)

    def test_hash(self):
        s = set()
        s.add(Note(PitchClass.C, 5))
        s.add(Note(PitchClass.C, 5))
        self.assertEqual(len(s), 1)

    def test_transpose(self):
        note = Note(PitchClass.C, 5)
        self.assertEqual(note.transpose(-1), Note(PitchClass.B, 4))
        self.assertEqual(note.transpose(12), Note(PitchClass.C, 6))

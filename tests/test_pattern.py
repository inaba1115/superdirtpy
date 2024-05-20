import unittest

from superdirtpy.pattern import Event


class TestEvent(unittest.TestCase):
    def test_validate(self):
        with self.assertRaises(ValueError):
            Event.validate({"delta": 1})
        with self.assertRaises(ValueError):
            Event.validate({"s": "bd"})

    def test_make_events_rest_note(self):
        params = {"s": None, "delta": 1}
        self.assertEqual(Event.make_events(params), [])

    def test_make_events_single_note(self):
        params = {"s": "bd", "delta": 1}
        self.assertEqual(Event.make_events(params), [{"s": "bd", "delta": 1}])

    def test_make_events_chord(self):
        params = {"s": "piano", "n": [0, 1], "delta": 1}
        self.assertEqual(
            Event.make_events(params),
            [{"s": "piano", "n": 0, "delta": 1}, {"s": "piano", "n": 1, "delta": 1}],
        )

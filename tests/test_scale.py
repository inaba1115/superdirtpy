import unittest

from superdirtpy.note import PitchClass
from superdirtpy.scale import Scale
from superdirtpy.scales import Scales


class TestScale(unittest.TestCase):
    def test_scale_bind(self):
        scale = Scale(PitchClass.C, Scales.min_pent)
        degrees = list(range(5))
        self.assertEqual(scale.bind(degrees=degrees, octave=5), [60, 63, 65, 67, 70])

        degrees = [0, None, 0]
        self.assertEqual(scale.bind(degrees=degrees, octave=5), [60, None, 60])

        degrees = [[0, 1, 2], [1, 2, 3]]
        self.assertEqual(
            scale.bind(degrees=degrees, octave=5), [[60, 63, 65], [63, 65, 67]]
        )

        degrees = list(range(-6, 7))
        self.assertEqual(
            scale.bind(degrees=degrees),
            [-14, -12, -9, -7, -5, -2, 0, 3, 5, 7, 10, 12, 15],
        )

    def test_get_pitch_classes(self):
        scale = Scale(PitchClass.A, Scales.min_pent)
        self.assertEqual(
            scale.get_pitch_classes(),
            [PitchClass.C, PitchClass.D, PitchClass.E, PitchClass.G, PitchClass.A],
        )
        self.assertEqual(scale.get_pitch_classes(), [0, 2, 4, 7, 9])

import logging
from datetime import timedelta

import numpy as np

import superdirtpy as sd

rng = np.random.default_rng()
client = sd.SuperDirtClient()
s = "mydevice"
midichan = 0


def main():
    tctx = sd.TemporalContext()

    e_add13 = sd.Scale(sd.PitchClass.E).bind(sd.Chords.add13)
    f_aug = sd.Scale(sd.PitchClass.F).bind(sd.Chords.aug)
    fs_nine_sus4 = sd.Scale(sd.PitchClass.Fs).bind(sd.Chords.nine_sus4)
    params = {
        "s": s,
        "midichan": midichan,
        "n": [e_add13, f_aug, fs_nine_sus4],
        "delta": [2, 2.5, 4],
        "amp": [0.7, 0.4, 0.5],
    }
    sd.Pattern(client=client, params=params).play(tctx)

    tctx.sleep(timedelta(seconds=1))

    params = {
        "s": s,
        "midichan": midichan,
        "n": sd.Scale(sd.PitchClass.D, sd.Scales.messiaen3).bind(rng.integers(-5, 15, 12).tolist()),
        "delta": [0.5, 0.3],
        "amp": 0.6,
    }
    sd.Pattern(client=client, params=params).play(tctx)

    params = {
        "s": s,
        "midichan": midichan,
        "n": sd.Scale(sd.PitchClass.A, sd.Scales.messiaen3).bind(rng.integers(-5, 15, 20).tolist()),
        "delta": 0.1,
        "amp": 0.5,
        "octave": 6,
    }
    sd.Pattern(client=client, params=params).play(tctx)


if __name__ == "__main__":
    try:
        logging.basicConfig(level=logging.DEBUG)
        main()
    except KeyboardInterrupt:
        pass

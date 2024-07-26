import numpy as np

import superdirtpy as sd

rng = np.random.default_rng()
client = sd.SuperDirtClient()
p = {"s": "superpiano"}
# p = {"s": "mydevice", "midichan": 0}


def main():
    tctx = sd.TemporalContext()
    scale = sd.Scale(sd.PitchClass.C, sd.Scales.messiaen3)

    for _ in range(16):
        n = rng.integers(1, 5, endpoint=True)
        degrees = rng.choice(10, n, replace=False).tolist()
        chord = scale.bind(degrees=degrees)

        params = p | {
            "n": [chord],
            "amp": rng.uniform(0.4, 0.9),
            "delta": rng.uniform(0.8, 2.0),
        }
        sd.Pattern(client=client, params=params).play(tctx)


if __name__ == "__main__":
    main()

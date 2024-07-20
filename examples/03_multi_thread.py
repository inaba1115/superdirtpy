import logging
from datetime import timedelta
from threading import Thread

import numpy as np

import superdirtpy as sd

client = sd.SuperDirtClient()


def main():
    tctx = sd.TemporalContext()
    now = tctx.now()

    def f1(tctx: sd.TemporalContext):
        for _ in range(4):
            params = {
                "s": np.resize(["hc", None], 16).tolist(),  # type: ignore
                "delta": 0.1,
            }
            sd.Pattern(client=client, params=params).play(tctx)

    def f2(tctx: sd.TemporalContext):
        for _ in range(4):
            params = {
                "s": np.resize(["bd", None, None], 16).tolist(),  # type: ignore
                "delta": 0.1,
            }
            sd.Pattern(client=client, params=params).play(tctx)

    ts = [
        Thread(target=f1, args=(tctx.clone(),)),
        Thread(target=f2, args=(tctx.clone(),)),
    ]
    [t.start() for t in ts]
    [t.join() for t in ts]
    tctx.sleep_until(now + timedelta(seconds=6.4))


if __name__ == "__main__":
    try:
        logging.basicConfig(level=logging.DEBUG)
        main()
    except KeyboardInterrupt:
        pass

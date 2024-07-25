import typing

import numpy as np

import superdirtpy as sd

rng = np.random.default_rng()
client = sd.SuperDirtClient()


class Markov:
    def __init__(
        self,
        xs: list[typing.Any],
        matrix: list[list[int]],
        rng: np.random.Generator | None = None,
    ) -> None:
        self.xs = xs
        self.matrix = self.__prepare(matrix)
        self.rng = np.random.default_rng(rng)

    def gen(self, n: int) -> list[typing.Any]:
        i = 0
        ret = []
        for _ in range(n):
            ret.append(self.xs[i])
            i = self.rng.choice(len(self.xs), p=self.matrix[i])
        return ret

    def __prepare(self, int_matrix: list[list[int]]) -> np.ndarray:
        matrix = np.array(int_matrix)
        return matrix / matrix.sum(axis=1).reshape(-1, 1)


def main():
    tctx = sd.TemporalContext()

    xs = ["bd", "sn", "hc", "ho", "can", None]
    matrix = [
        [1, 1, 0, 1, 0, 0],
        [1, 0, 1, 0, 0, 1],
        [0, 0, 0, 1, 1, 1],
        [0, 1, 0, 1, 0, 1],
        [1, 0, 1, 1, 0, 0],
        [1, 0, 1, 0, 0, 1],
    ]
    m = Markov(xs, matrix)

    for _ in range(8):
        params = {
            "s": m.gen(16),
            "delta": 0.2,
        }
        sd.Pattern(client=client, params=params).play(tctx)


if __name__ == "__main__":
    main()

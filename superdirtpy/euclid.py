def euclid(k: int, n: int, r: int = 0) -> str:
    if n < 1:
        raise ValueError(f"n must be a positive value: n={n}")
    if k > n:
        raise ValueError(f"k must be smaller than or equal to n: k={k}, n={n}")

    xss, yss = [["x"] for _ in range(k)], [["."] for _ in range(n - k)]
    xss, yss = _euclid(xss, yss)
    xs = sum(xss + yss, [])
    r %= len(xs)
    xs = xs[r:] + xs[:r]
    return "".join(xs)


def _euclid(
    xss: list[list[str]], yss: list[list[str]]
) -> tuple[list[list[str]], list[list[str]]]:
    size = min(len(xss), len(yss))
    for i in range(size):
        xss[i] += yss[i]
    xss, yss = xss[:size], xss[size:] + yss[size:]
    if len(yss) < 2:
        return xss, yss
    return _euclid(xss, yss)

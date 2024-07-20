from datetime import timedelta
from threading import Lock, Thread

from lark import Lark, Transformer, v_args

import superdirtpy as sd

pattern_grammer = r"""
    pattern: unit+

    ?unit: list | note

    list: "[" unit+ "]"

    note: "~" -> rest
        | WORD -> sound

    %import common.WORD
    %import common.WS
    %ignore WS
"""


class PatternTransformer(Transformer):
    pattern = list
    list = list

    def rest(self, _):
        return None

    @v_args(inline=True)
    def sound(self, s):
        return str(s)


pattern_parser = Lark(
    pattern_grammer, parser="lalr", start="pattern", transformer=PatternTransformer()
)


def make_sound_delta(pattern: list, sec: float) -> tuple[list[str], list[float]]:
    ret_sound = []
    ret_delta = []
    unit_delta = sec / len(pattern)
    for unit in pattern:
        if isinstance(unit, list):
            sound, delta = make_sound_delta(unit, unit_delta)
            ret_sound.extend(sound)
            ret_delta.extend(delta)
        else:
            ret_sound.append(unit)
            ret_delta.append(unit_delta)
    return ret_sound, ret_delta


def bpm_to_sec_per_cycle(bpm: float) -> float:
    return 60 / bpm * 4


bpm = 180
pattern_global = "bd [bd sn] ho [bd sn]"
lock = Lock()


def player():
    sec_per_cycle = bpm_to_sec_per_cycle(bpm)
    client = sd.SuperDirtClient()
    tctx = sd.TemporalContext()
    pattern_cache = ""

    while True:
        now = tctx.now()

        with lock:
            if pattern_cache != pattern_global:
                pattern_cache = pattern_global
                pattern_updated = True
                print(f"current pattern = {pattern_cache}")

        if pattern_cache != "":
            if pattern_updated:
                pattern = pattern_parser.parse(pattern_cache)
                sound, delta = make_sound_delta(pattern, sec_per_cycle)  # type: ignore
                pattern_updated = False

            params = {
                "s": sound,
                "delta": delta,
                "shape": 0.8,
                "coarse": 16,
                "room": 0.6,
                "size": 0.6,
            }
            sd.Pattern(client=client, params=params).play(tctx)

        tctx.sleep_until(now + timedelta(seconds=sec_per_cycle))


def main():
    global pattern_global

    t = Thread(target=player)
    t.daemon = True
    t.start()

    while True:
        try:
            s = input()
        except KeyboardInterrupt:
            break

        with lock:
            pattern_global = s


if __name__ == "__main__":
    main()

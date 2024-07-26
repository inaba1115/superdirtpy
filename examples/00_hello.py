import superdirtpy as sd

client = sd.SuperDirtClient()


def main():
    tctx = sd.TemporalContext()

    for _ in range(8):
        params = {
            "sound": ["bd", "sn:1"],
            "delta": 0.5,
        }
        sd.Pattern(client=client, params=params).play(tctx)


if __name__ == "__main__":
    main()

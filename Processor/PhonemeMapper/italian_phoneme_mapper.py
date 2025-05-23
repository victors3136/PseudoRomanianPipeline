class ItalianPhonemeMapper:
    __It2Ro = {
        # vowels
        "a": "a",
        "e": "e",
        "ɛ": "e",
        "i": "i",
        "o": "o",
        "ɔ": "o",
        "u": "u",
        # consonants
        "b": "b",
        "d": "d",
        "t": "t",
        "k": "k",
        "g": "ɡ",
        "ɡ": "ɡ",
        "p": "p",
        "f": "f",
        "v": "v",
        "s": "s",
        "z": "z",
        "m": "m",
        "n": "n",
        "ɲ": "nj",
        "ʎ": "lj",
        "l": "l",
        "ll": "l",
        "r": "r",
        "ɾ": "r",
        "ttʃ": "tʃ",
        "tʃ": "tʃ",
        "ddʒ": "dʒ",
        "dʒ": "dʒ",
        "tts": "ts",
        "ts": "ts",
        "ddz" : "ts",
        "dz": "ts",
        "w": "u",
        "j": "j",
        "ʃ": "ʃ"
    }
    # sorted so that we check for longer constructs first
    # e.g. check for 'tʃ' before checking for 't'
    __It2RoKeys = sorted(__It2Ro.keys(), key=len, reverse=True)

    @classmethod
    def keys(cls) -> list:
        return cls.__It2RoKeys

    @classmethod
    def dict(cls) -> dict:
        return cls.__It2Ro

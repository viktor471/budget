from typing import Iterable

def OnlyOneIsTrue(*args) -> bool:
    def check(iterable: Iterable):
        assert isinstance(iterable, Iterable)

        return [bool(it) for it in iterable].count(True) == 1

    assert len(args) >= 1, "wrong amount of arguments"

    return check(args) if len(args) > 1 else check(args[0])

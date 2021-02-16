from enum import Enum


class ActualIs(Enum):
    HIGHER = 1
    MATCH = 0
    LOWER = -1


def higher_lower(min_value, max_value, callback):
    assert isinstance(max_value, int)
    assert isinstance(min_value, int)
    assert max_value > min_value
    candidate = midpoint(min_value, max_value)
    while True:
        result = callback(candidate)
        if result is ActualIs.MATCH:
            return candidate
        elif result is ActualIs.LOWER:
            # lower
            max_value = candidate
            candidate = midpoint(min_value, candidate)
        elif result is ActualIs.HIGHER:
            # higher
            min_value = candidate
            candidate = midpoint(candidate, max_value)
        else:
            assert False, "Should be a ActualIs enum constant"


def midpoint(x, y):
    mid = x + ((y - x) // 2)
    return mid

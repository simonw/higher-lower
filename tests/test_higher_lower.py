from hypothesis import given
import hypothesis.strategies as st
from higher_lower import higher_lower, midpoint, ActualIs
import pytest
import sys


SYS_MIN = -sys.maxsize
SYS_MAX = sys.maxsize


@pytest.mark.parametrize(
    "x,y,expected",
    (
        (0, 10, 5),
        (-10, 10, 0),
        (0, 1, 0),
        (0, 3, 1),
        (-10, -10, -10),
    ),
)
def test_midpoint(x, y, expected):
    assert midpoint(x, y) == expected


def test_higher_lower_basic():
    callback = make_callback(4)
    result = higher_lower(0, 10, callback)
    assert result == 4


@given(st.integers(min_value=SYS_MIN, max_value=SYS_MAX))
def test_higher_lower_with_hypothesis(integer):
    assert higher_lower(SYS_MIN, SYS_MAX, make_callback(integer)) == integer


def make_callback(integer):
    def callback(candidate):
        if candidate == integer:
            return ActualIs.MATCH
        elif candidate > integer:
            return ActualIs.LOWER
        else:
            return ActualIs.HIGHER

    return callback

import pytest

from task1.solution import strict


@strict
def sum_two(a: int, b: int):
    return a + b


def test_strict_ok():
    assert sum_two(2, b=True) == 3


def test_strict_type_error():
    with pytest.raises(TypeError):
        sum_two(2, b=2.4)

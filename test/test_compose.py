from typing import TypeVar

import pytest
from compose import compose, sequential
from typing_extensions import assert_type

V = TypeVar("V", int, float)


def a(x):
    print(f"a({x}) was called, adding 1")
    return x + 1


def b(x):
    print(f"b({x}) was called, squaring")
    return x**2


def c(x):
    print(f"c({x}) was called, dividing by 2")
    return x / 2


@pytest.mark.parametrize("x", [1, 2, 3, 12.1])
def test_order_of_composition(x):
    assert compose(a, b, c)(x) == c(b(a(x)))
    assert sequential(a, b, c)(x) == a(b(c(x)))

    assert compose(a, b, c, c, c)(x) == c(c(c(b(a(x)))))
    assert sequential(a, b, c, c, c)(x) == a(b(c(c(c(x)))))


def is_even(x: int) -> bool:
    assert isinstance(x, int)
    return x % 2 == 0


def square(x: V) -> V:
    return x**2


def float_to_int(x: float) -> int:
    return round(x)


def test_type_errors():
    bad_f = compose(float, str, round)  # get a type error here!
    with pytest.raises(TypeError):
        bad_f(1.2)


def test_type_hints():
    good_f = compose(
        square,
        float_to_int,
        is_even,
        str,
        bool,
        bool,
        bool,
        bool,
        float,
        float,
        int,
        float,
        bool,
        float,
        bool,
        square,
    )

    # print(good_f(1.2))

    abc = compose(a, b, c)
    cba = compose(*reversed([a, b, c]))


if __name__ == "__main__":
    main()

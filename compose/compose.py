from __future__ import annotations
import functools
import typing
from typing import Any, Callable, TypeVar, overload

if typing.TYPE_CHECKING:
    from typing_extensions import ParamSpec, Unpack

    # In = TypeVar("In")
    Out = TypeVar("Out")
    A = TypeVar("A")
    B = TypeVar("B")
    C = TypeVar("C")
    D = TypeVar("D")
    E = TypeVar("E")
    F = TypeVar("F")
    G = TypeVar("G")
    H = TypeVar("H")
    T = TypeVar("T")
    In = ParamSpec("In")


@overload
def compose(fn_a: Callable[In, Out], /) -> Callable[In, Out]:
    ...


@overload
def compose(
    fn_b: Callable[[A], Out],
    fn_a: Callable[In, A],
    /,
) -> Callable[In, Out]:
    ...


@overload
def compose(
    fn_c: Callable[[B], Out],
    fn_b: Callable[[A], B],
    fn_a: Callable[In, A],
    /,
) -> Callable[In, Out]:
    ...


@overload
def compose(
    fn_d: Callable[[C], Out],
    fn_c: Callable[[B], C],
    fn_b: Callable[[A], B],
    fn_a: Callable[In, A],
    /,
) -> Callable[In, Out]:
    ...


@overload
def compose(
    fn_e: Callable[[D], Out],
    fn_d: Callable[[C], D],
    fn_c: Callable[[B], C],
    fn_b: Callable[[A], B],
    fn_a: Callable[In, A],
    /,
) -> Callable[In, Out]:
    ...


@overload
def compose(
    fn_f: Callable[[E], Out],
    fn_e: Callable[[D], E],
    fn_d: Callable[[C], D],
    fn_c: Callable[[B], C],
    fn_b: Callable[[A], B],
    fn_a: Callable[In, A],
    /,
) -> Callable[In, Out]:
    ...


@overload
def compose(
    fn_f: Callable[[E], Out],
    fn_e: Callable[[D], E],
    fn_d: Callable[[C], D],
    fn_c: Callable[[B], C],
    fn_b: Callable[[A], B],
    fn_a: Callable[In, A],
    /,
) -> Callable[In, Out]:
    ...


@overload
def compose(
    fn_a: Callable[[B], Out],
    /,
    *other_fns: Unpack[
        tuple[Callable[[A], B], Unpack[tuple[Callable[[A], A], ...]], Callable[In, A]]
    ],
) -> Callable[In, Out]:
    ...


def compose(
    *callables: Unpack[
        tuple[
            Callable[[A], Out],
            Unpack[tuple[Unpack[tuple[Callable[[A], A], ...]], Callable[In, A]]],
        ]
    ],
) -> Callable[In, Out]:
    """Compose multiple functions or callables into a single callable.

    Take note of the ordering:
    `compose(a, b, c)(x) == c(b(a(x)))`
    """
    return functools.reduce(
        _compose_two_functions,
        reversed(callables),
    )


def _inner(
    fn_a: Callable[[A], Out], fn_b: Callable[In, A], /, *args: In.args, **kwargs: In.kwargs
) -> Out:
    return fn_a(fn_b(*args, **kwargs))


def _compose_two_functions(fn_a: Callable[[A], Out], fn_b: Callable[In, A]) -> Callable[In, Out]:
    return functools.partial(_inner, fn_a, fn_b)  # type: ignore (pylance doesn't get that it's OK)


# @overload
# def sequential(fn_a: Callable[In, Out], /) -> Callable[In, Out]:
#     ...


@overload
def sequential(
    fn_a: Callable[In, A],
    fn_b: Callable[[A], Out],
    /,
) -> Callable[In, Out]:
    ...


@overload
def sequential(
    fn_a: Callable[In, A],
    fn_b: Callable[[A], B],
    fn_c: Callable[[B], Out],
    /,
) -> Callable[In, Out]:
    ...


@overload
def sequential(
    fn_a: Callable[In, A],
    fn_b: Callable[[A], B],
    fn_c: Callable[[B], C],
    fn_d: Callable[[C], Out],
    /,
) -> Callable[In, Out]:
    ...


@overload
def sequential(
    fn_a: Callable[In, A],
    fn_b: Callable[[A], B],
    fn_c: Callable[[B], C],
    fn_d: Callable[[C], D],
    fn_e: Callable[[D], Out],
    /,
) -> Callable[In, Out]:
    ...


@overload
def sequential(
    fn_a: Callable[In, A],
    fn_b: Callable[[A], B],
    fn_c: Callable[[B], C],
    fn_d: Callable[[C], D],
    fn_e: Callable[[D], E],
    fn_f: Callable[[E], Out],
    /,
) -> Callable[In, Out]:
    ...


@overload
def sequential(
    fn_a: Callable[In, A],
    fn_b: Callable[[A], B],
    fn_c: Callable[[B], C],
    fn_d: Callable[[C], D],
    fn_e: Callable[[D], E],
    fn_f: Callable[[E], F],
    /,
    *other_fns: Unpack[
        tuple[Callable[[E], F], Unpack[tuple[Callable[[G], G], ...]], Callable[[G], Out]]
    ],
) -> Callable[In, Out]:
    ...


def sequential(
    *callables: Unpack[
        tuple[
            Callable[In, T],
            Unpack[
                tuple[
                    Unpack[tuple[Callable, ...]],
                    Callable[[T], Out],
                ]
            ],
        ]
    ],
) -> Callable[In, Out]:
    """Returns a callable that applies the functions in sequence.

    Take note of the ordering: `sequential(a, b, c)(x) == c(b(a(x)))`
    """
    return compose(*reversed(callables))  # type: ignore (Pylance doesn't get that it's OK)

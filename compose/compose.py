from __future__ import annotations
import typing
from typing import Any, Callable, TypeVar, overload

if typing.TYPE_CHECKING:
    from typing_extensions import ParamSpec, Unpack

    A = TypeVar("A")
    B = TypeVar("B")
    C = TypeVar("C")
    D = TypeVar("D")
    E = TypeVar("E")
    F = TypeVar("F")
    G = TypeVar("G")
    H = TypeVar("H")
    T = TypeVar("T")
    P = ParamSpec("P")


@overload
def compose(fn_a: Callable[P, A], /) -> Callable[P, A]:
    ...


@overload
def compose(
    fn_a: Callable[P, A],
    fn_b: Callable[[A], B],
    /,
) -> Callable[P, B]:
    ...


@overload
def compose(
    fn_a: Callable[P, A],
    fn_b: Callable[[A], B],
    fn_c: Callable[[B], C],
    /,
) -> Callable[P, C]:
    ...


@overload
def compose(
    fn_a: Callable[P, A],
    fn_b: Callable[[A], B],
    fn_c: Callable[[B], C],
    fn_d: Callable[[C], D],
    /,
) -> Callable[P, D]:
    ...


@overload
def compose(
    fn_a: Callable[P, A],
    fn_b: Callable[[A], B],
    fn_c: Callable[[B], C],
    fn_d: Callable[[C], D],
    fn_e: Callable[[D], E],
    /,
) -> Callable[P, E]:
    ...


@overload
def compose(
    fn_a: Callable[P, A],
    fn_b: Callable[[A], B],
    fn_c: Callable[[B], C],
    fn_d: Callable[[C], D],
    fn_e: Callable[[D], E],
    fn_f: Callable[[E], F],
    /,
) -> Callable[P, F]:
    ...


@overload
def compose(
    fn_a: Callable[P, A],
    fn_b: Callable[[A], B],
    fn_c: Callable[[B], C],
    fn_d: Callable[[C], D],
    fn_e: Callable[[D], E],
    fn_f: Callable[[E], F],
    /,
) -> Callable[P, F]:
    ...


@overload
def compose(
    fn_a: Callable[P, A],
    fn_b: Callable[[A], B],
    fn_c: Callable[[B], C],
    fn_d: Callable[[C], D],
    fn_e: Callable[[D], E],
    fn_f: Callable[[E], F],
    /,
    *other_fns: Unpack[
        tuple[Callable[[E], F], Unpack[tuple[Callable[[G], G], ...]], Callable[[G], H]]
    ],
) -> Callable[P, H]:
    ...


def compose(
    first_function: Callable[P, Any],
    /,
    *callables: Unpack[tuple[Unpack[tuple[Callable, ...]], Callable[[Any], A]]],
) -> Callable[P, A]:
    """Compose multiple functions or callables into a single callable.

    `compose(a, b, c)` is the same as `lambda x: (a(b(c(x))))`
    """

    def _inner(*args: P.args, **kwagrs: P.kwargs):
        out = first_function(*args, **kwagrs)
        for callable in callables:
            out = callable(out)
        return out

    return _inner

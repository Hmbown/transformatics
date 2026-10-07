from __future__ import annotations

from typing import Any, Callable, Generic, TypeVar

from .core import Observable, Transformation

State = TypeVar("State")
Scalar = TypeVar("Scalar")


def shift(T: Transformation[State], f: Observable[State, Scalar]) -> Observable[State, Scalar]:
    """Shift operator U_T f = f ∘ T."""

    return Observable(lambda x: f(T(x)), name=f"U_{T.name or 'T'}({f.name or 'f'})")


def resolvant(T: Transformation[State], f: Observable[State, Scalar]) -> Observable[State, Scalar]:
    """Resolvant ∇_T f = f∘T - f (finite update)."""

    return Observable(
        lambda x: f(T(x)) - f(x),  # type: ignore
        name=f"∇_{T.name or 'T'}({f.name or 'f'})",
    )


def accumulation(T: Transformation[State], f: Observable[State, Scalar], x0: State, N: int) -> Scalar:
    """Accumulation A_T^N f(x0) = Σ_{k=0..N-1} ∇_T f(T^k(x0)).

    Telescopes exactly to f(T^N(x0)) - f(x0).
    """

    if N < 0:
        raise ValueError("N must be >= 0")

    df = resolvant(T, f)
    
    if N == 0:
        val = df(x0)
        return val * 0  # type: ignore

    total = df(x0)
    x = T(x0)
    for _ in range(1, N):
        total = total + df(x)  # type: ignore
        x = T(x)
    return total  # type: ignore

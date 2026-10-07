from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Generic, Iterable, Iterator, TypeVar

State = TypeVar("State")
Scalar = TypeVar("Scalar")


@dataclass(frozen=True)
class Transformation(Generic[State]):
    """A deterministic state update T: X -> X.

    Composition is *function composition*: (T ∘ S)(x) = T(S(x)).
    """

    rule: Callable[[State], State]
    name: str | None = None

    def __call__(self, x: State) -> State:
        return self.rule(x)

    def compose(self, other: "Transformation[State]") -> "Transformation[State]":
        # (self ∘ other)(x) = self(other(x))
        nm = None
        if self.name or other.name:
            nm = f"({self.name or 'T'}∘{other.name or 'S'})"
        return Transformation(lambda x: self.rule(other.rule(x)), name=nm)

    def power(self, n: int) -> "Transformation[State]":
        if n < 0:
            raise ValueError("power(n): n must be >= 0 for deterministic forward iteration")
        if n == 0:
            return Transformation(lambda x: x, name="I")
        t = self
        for _ in range(n - 1):
            t = t.compose(self)
        return t

    def orbit(self, x0: State, steps: int) -> Iterator[State]:
        """Yield x0, T(x0), ..., T^steps(x0)."""
        if steps < 0:
            raise ValueError("steps must be >= 0")
        x = x0
        yield x
        for _ in range(steps):
            x = self(x)
            yield x


@dataclass(frozen=True)
class Observable(Generic[State, Scalar]):
    """An observable f: X -> Scalar (often float)."""

    func: Callable[[State], Scalar]
    name: str | None = None

    def __call__(self, x: State) -> Scalar:
        return self.func(x)

    def map(self, g: Callable[[Scalar], Scalar], name: str | None = None) -> "Observable[State, Scalar]":
        nm = name or (f"{g.__name__}({self.name})" if self.name else None)
        return Observable(lambda x: g(self.func(x)), name=nm)

    @staticmethod
    def from_attr(attr: str, name: str | None = None) -> "Observable[object, object]":
        return Observable(lambda x: getattr(x, attr), name=name or attr)

from collections.abc import Iterable
from dataclasses import dataclass

from tatar_morph.types import (
    AnyType,
)


@dataclass(slots=True, frozen=True, init=False)
class ParsingResults:
    _features: tuple[AnyType, ...]

    def __init__(self, features: Iterable[AnyType]) -> None:
        object.__setattr__(self, "_features", tuple(features))

    def get_all[FeatureT: AnyType](
        self, feature_type: type[FeatureT]
    ) -> tuple[FeatureT, ...]:
        return tuple(feature for feature in self._features if type(feature) is feature_type)

    def all(self) -> tuple[AnyType, ...]:
        return self._features

    def __repr__(self) -> str:
        return f"ParsingResults{self._features!s}"


@dataclass(slots=True, frozen=True, kw_only=True)
class Analysis:
    word: str
    lemma: str
    features: ParsingResults
    weight: float
    raw_tags: tuple[str, ...]


@dataclass(slots=True, frozen=True, kw_only=True)
class GenerationResult:
    word: str
    weight: float

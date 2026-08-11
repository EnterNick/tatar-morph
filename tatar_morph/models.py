from dataclasses import dataclass

from tatar_morph.types import (
    PartOfSpeech,
    AnyType,
)


class ParsingResults:
    def __init__(self, features: list[AnyType]) -> None:
        self._features = features

    def get[FeatureT: AnyType](self, feature_type: type[FeatureT]) -> FeatureT | None:
        return next(
            filter(lambda feature: type(feature) is feature_type, self._features), None
        )

    def list(self) -> list[AnyType]:
        return list(self._features)

    def __repr__(self):
        return f"ParsingResults{self._features!s}"


@dataclass(slots=True, frozen=True, kw_only=True)
class Analysis:
    word: str
    lemma: str
    pos: PartOfSpeech
    features: ParsingResults
    weight: float
    tags: list[str]

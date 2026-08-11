from dataclasses import dataclass
from typing import Protocol
from collections.abc import Iterable

from tatar_morph.models import ParsingResults, Analysis


@dataclass(slots=True)
class EngineData:
    word: str
    weight: float


class IDataDecoder[EngResultT](Protocol):
    def parse_list(self, data: Iterable[EngResultT]) -> Iterable[EngineData]:
        pass

    def lemmatize(self, data: EngResultT) -> str:
        pass

    def parse_features(self, data: EngResultT) -> tuple[ParsingResults, tuple[str, ...]]:
        pass

    def generate(self, lemma: str, tags: Iterable[str]) -> str:
        pass

    def decode(self, word: str, data: EngResultT) -> Analysis:
        pass

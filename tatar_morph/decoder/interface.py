from collections.abc import Iterable
from typing import Protocol

from tatar_morph.models import Analysis, GenerationResult, ParsingResults
from tatar_morph.types import AnyType


class IDataDecoder[AnalyzeResultT, GenerateQueryT, GenerateResultT](Protocol):
    def lemmatize(self, data: AnalyzeResultT) -> str:
        pass

    def parse_features(
        self, data: AnalyzeResultT
    ) -> tuple[ParsingResults, tuple[str, ...]]:
        pass

    def encode_generation(
        self, lemma: str, features: Iterable[AnyType]
    ) -> GenerateQueryT:
        pass

    def decode(self, word: str, data: AnalyzeResultT) -> Analysis:
        pass

    def decode_generation(self, data: GenerateResultT) -> GenerationResult:
        pass

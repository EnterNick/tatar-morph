from collections.abc import Iterable
from typing import Protocol


class MorphologyEngine[AnalyzeResultT, GenerateQueryT, GenerateResultT](Protocol):
    def analyze(self, word: str) -> Iterable[AnalyzeResultT]: ...

    def generate(self, query: GenerateQueryT) -> Iterable[GenerateResultT]: ...

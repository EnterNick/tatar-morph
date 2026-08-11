from typing import Protocol
from collections.abc import Iterable


class MorphologyEngine[EngResultT](Protocol):
    def analyze(self, word: str) -> Iterable[EngResultT]:
        pass

    def generate(self, lexical_form: str) -> Iterable[EngResultT]:
        pass

from typing import Protocol


class MorphologyEngine(Protocol):
    def analyze(self, word: str) -> list[tuple[str, int]]:
        pass

    def generate(self, lexical_form: str) -> list[tuple[str, float]]:
        pass

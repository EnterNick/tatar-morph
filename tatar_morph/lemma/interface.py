from typing import Protocol


class ILemmaParser(Protocol):
    def lemmatize(self, word: str) -> str:
        pass

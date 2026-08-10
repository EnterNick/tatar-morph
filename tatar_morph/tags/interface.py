from collections.abc import Iterable

from tatar_morph.models import ParsingResults
from tatar_morph.types import PartOfSpeech, AnyType


class ITagsMapper:
    def parse(self, word: str) -> tuple[PartOfSpeech, ParsingResults, list[str]]:
        pass

    def resolve(self, lemma: str, tags: Iterable[str]) -> str:
        pass

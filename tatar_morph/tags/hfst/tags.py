import re
from collections.abc import Iterable

from tatar_morph.models import ParsingResults
from tatar_morph.tags.hfst.known import KNOWN_SYMBOLS_MAPPER
from tatar_morph.types import PartOfSpeech, AnyType

KNOWN_SYMBOLS: frozenset[str] = frozenset(KNOWN_SYMBOLS_MAPPER.keys())
TAG_RE = re.compile(r"<([^<>]+)>")


class HFSTTagsParser:
    def parse(self, word: str) -> tuple[PartOfSpeech, ParsingResults, list[str]]:
        pos, *raw_tags = self._parse_tags(word)
        parsed_results = list(filter(bool, map(KNOWN_SYMBOLS_MAPPER.get, raw_tags)))
        return (
            PartOfSpeech(KNOWN_SYMBOLS_MAPPER[pos]),
            ParsingResults(parsed_results),
            raw_tags,
        )

    def resolve(self, lemma: str, tags: Iterable[str]) -> str:
        raw_tags = "><".join(tags)
        return f"{lemma}<{raw_tags}>"

    def _parse_tags(self, string: str) -> list[str]:
        return TAG_RE.findall(string)

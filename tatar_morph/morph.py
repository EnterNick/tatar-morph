from typing import Any
from collections.abc import Generator, Iterable

from tatar_morph.engines.base import MorphologyEngine
from tatar_morph.lemma.interface import ILemmaParser
from tatar_morph.models import Analysis
from tatar_morph.tags.interface import ITagsMapper


class TatarMorph:
    def __init__(
        self,
        engine: MorphologyEngine,
        tags_parser: ITagsMapper,
        lemma_parser: ILemmaParser,
    ) -> None:
        self._engine = engine
        self._tags_parser = tags_parser
        self._lemma_parser = lemma_parser

    def parse(self, word: str) -> Generator[Analysis, Any, None]:
        word = self._normalize_word(word)
        raw_analysis = self._engine.analyze(word)
        for suggest, weight in raw_analysis:
            pos, features, raw_tags = self._tags_parser.parse(suggest)
            lemma = self._lemma_parser.lemmatize(suggest)
            yield Analysis(
                word=word,
                pos=pos,
                weight=weight,
                features=features,
                tags=raw_tags,
                lemma=lemma,
            )

    def lemmatize(self, word: str) -> list[str]:
        word = self._normalize_word(word)
        raw_analysis = (x[0] for x in self._engine.analyze(word))
        return [*dict.fromkeys(map(self._lemma_parser.lemmatize, raw_analysis))]

    def generate(
        self, lemma: str, tags: Iterable[str]
    ) -> Generator[tuple[str, float], Any, None]:
        lemma = self._normalize_word(lemma)
        yield from self._engine.generate(self._tags_parser.resolve(lemma, tags))

    def _normalize_word(self, word: str) -> str:
        return word.lower().strip()

from collections.abc import Iterable, Iterator

from tatar_morph.engines.base import MorphologyEngine
from tatar_morph.decoder.interface import IDataDecoder
from tatar_morph.models import Analysis


class TatarMorph[EngResultT]:
    def __init__(
        self,
        engine: MorphologyEngine[EngResultT],
        data_decoder: IDataDecoder[EngResultT],
    ) -> None:
        self._engine = engine
        self._data_parser = data_decoder

    def parse(self, word: str) -> Iterator[Analysis]:
        word = self._normalize_word(word)
        raw_analysis = self._engine.analyze(word)
        for raw_data in raw_analysis:
            yield self._data_parser.decode(word, raw_data)

    def lemmatize(self, word: str) -> list[str]:
        word = self._normalize_word(word)
        return [
            *dict.fromkeys(map(self._data_parser.lemmatize, self._engine.analyze(word)))
        ]

    def generate(self, lemma: str, tags: Iterable[str]) -> Iterator[tuple[str, float]]:
        lemma = self._normalize_word(lemma)
        raw_datas = self._engine.generate(self._data_parser.generate(lemma, tags))
        for data in self._data_parser.parse_list(raw_datas):
            yield data.word, data.weight

    def _normalize_word(self, word: str) -> str:
        return word.lower().strip()

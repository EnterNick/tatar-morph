from collections.abc import Callable, Iterable, Iterator

from tatar_morph.decoder.interface import IDataDecoder
from tatar_morph.engines.base import MorphologyEngine
from tatar_morph.models import Analysis


def normalize_word(word: str) -> str:
    return word.lower().strip()


class TatarMorph[AnalyzeResultT, GenerateQueryT, GenerateResultT]:
    def __init__(
        self,
        engine: MorphologyEngine[AnalyzeResultT, GenerateQueryT, GenerateResultT],
        data_decoder: IDataDecoder[AnalyzeResultT, GenerateQueryT, GenerateResultT],
        normalizer: Callable[[str], str] = normalize_word,
    ) -> None:
        self._engine = engine
        self._data_decoder = data_decoder
        self._normalizer = normalizer

    def parse(self, word: str) -> Iterator[Analysis]:
        word = self._normalizer(word)
        raw_analysis = self._engine.analyze(word)
        for raw_data in raw_analysis:
            yield self._data_decoder.decode(word, raw_data)

    def lemmatize(self, word: str) -> list[str]:
        word = self._normalizer(word)
        return [
            *dict.fromkeys(map(self._data_decoder.lemmatize, self._engine.analyze(word)))
        ]

    def generate(self, lemma: str, tags: Iterable[str]) -> Iterator[tuple[str, float]]:
        lemma = self._normalizer(lemma)
        query = self._data_decoder.encode_generation(lemma, tags)
        for raw_data in self._engine.generate(query):
            data = self._data_decoder.decode_generation(raw_data)
            yield data.word, data.weight

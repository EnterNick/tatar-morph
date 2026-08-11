from collections.abc import Iterable
import re

from tatar_morph.decoder.hfst.known import KNOWN_SYMBOLS_MAPPER
from tatar_morph.decoder.interface import EngineData
from tatar_morph.models import ParsingResults, Analysis

TAG_RE = re.compile(r"<([^<>]+)>")


class HFSTDataDecoder:
    def parse_list(self, data: Iterable[tuple[str, float]]) -> Iterable[EngineData]:
        return map(self._parse, data)

    def parse_features(
        self, data: tuple[str, float]
    ) -> tuple[ParsingResults, tuple[str, ...]]:
        raw_tags = self._parse_tags(data[0])
        features = (KNOWN_SYMBOLS_MAPPER.get(tag) for tag in raw_tags)
        return ParsingResults(
            feature for feature in features if feature is not None
        ), raw_tags

    def generate(self, lemma: str, tags: Iterable[str]) -> str:
        tags = tuple(tags)
        if not tags:
            raise ValueError("At least one morphology tag is required")
        raw_tags = "><".join(tags)
        return f"{lemma}<{raw_tags}>"

    def lemmatize(self, data: tuple[str, float]) -> str:
        return data[0].split("<", maxsplit=1)[0]

    def decode(self, word: str, data: tuple[str, float]) -> Analysis:
        encoded = self._parse(data)
        features, raw_tags = self.parse_features(data)
        lemma = self.lemmatize(data)
        return Analysis(
            word=word,
            weight=encoded.weight,
            features=features,
            raw_tags=raw_tags,
            lemma=lemma,
        )

    def _parse_tags(self, string: str) -> tuple[str, ...]:
        return tuple(TAG_RE.findall(string))

    def _parse(self, data: tuple[str, float]) -> EngineData:
        return EngineData(
            word=data[0],
            weight=data[1],
        )

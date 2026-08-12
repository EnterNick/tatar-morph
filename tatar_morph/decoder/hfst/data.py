from collections.abc import Iterable
import re

from tatar_morph.decoder.hfst.known import (
    FEATURE_TO_KNOWN_SYMBOL,
    KNOWN_SYMBOLS_MAPPER,
)
from tatar_morph.exceptions import UnsupportedGenerationFeatureError
from tatar_morph.models import Analysis, GenerationResult, ParsingResults
from tatar_morph.types import AnyType

TAG_RE = re.compile(r"<([^<>]+)>")


class HFSTDataDecoder:
    def parse_features(
        self, data: tuple[str, float]
    ) -> tuple[ParsingResults, tuple[str, ...]]:
        raw_tags = self._parse_tags(data[0])
        features = (KNOWN_SYMBOLS_MAPPER.get(tag) for tag in raw_tags)
        return ParsingResults(
            feature for feature in features if feature is not None
        ), raw_tags

    def encode_generation(self, lemma: str, features: Iterable[AnyType]) -> str:
        features = tuple(features)
        if not features:
            raise ValueError("At least one morphology feature is required")
        tags = tuple(self._encode_feature(feature) for feature in features)
        raw_tags = "><".join(tags)
        return f"{lemma}<{raw_tags}>"

    def lemmatize(self, data: tuple[str, float]) -> str:
        return data[0].split("<", maxsplit=1)[0]

    def decode(self, word: str, data: tuple[str, float]) -> Analysis:
        features, raw_tags = self.parse_features(data)
        lemma = self.lemmatize(data)
        return Analysis(
            word=word,
            weight=data[1],
            features=features,
            raw_tags=raw_tags,
            lemma=lemma,
        )

    def decode_generation(self, data: tuple[str, float]) -> GenerationResult:
        return GenerationResult(word=data[0], weight=data[1])

    def _parse_tags(self, string: str) -> tuple[str, ...]:
        return tuple(TAG_RE.findall(string))

    @staticmethod
    def _encode_feature(feature: AnyType) -> str:
        try:
            return FEATURE_TO_KNOWN_SYMBOL[(type(feature), feature)]
        except KeyError as error:
            raise UnsupportedGenerationFeatureError(
                f"HFST cannot encode morphology feature: {feature!r}"
            ) from error

from collections.abc import Iterable

import pytest

from tatar_morph.models import Analysis, GenerationResult, ParsingResults
from tatar_morph.morph import TatarMorph
from tatar_morph.types import AnyType, PartOfSpeech

type FakeRawResult = tuple[str, float]
type FakeMorph = TatarMorph[FakeRawResult, str, FakeRawResult]


class FakeEngine:
    def __init__(self) -> None:
        self.analyzed_words: list[str] = []
        self.generated_forms: list[str] = []

    def analyze(self, word: str) -> list[tuple[str, float]]:
        self.analyzed_words.append(word)
        return [(f"{word}<n><nom>", 0.25)]

    def generate(self, lexical_form: str) -> list[tuple[str, float]]:
        self.generated_forms.append(lexical_form)
        return [("Өй", 0.5)]


class FakeDataDecoder:
    def lemmatize(self, data: tuple[str, float]) -> str:
        return data[0].split("<", maxsplit=1)[0]

    def parse_features(
        self, data: tuple[str, float]
    ) -> tuple[ParsingResults, tuple[str, ...]]:
        return ParsingResults([PartOfSpeech.NOUN]), ("n", "nom")

    def encode_generation(
        self, lemma: str, features: Iterable[AnyType]
    ) -> str:
        features = tuple(features)
        if not features:
            raise ValueError("At least one morphology feature is required")
        return f"{lemma}<{'><'.join(feature.value for feature in features)}>"

    def decode(self, word: str, raw_data: tuple[str, float]) -> Analysis:
        return Analysis(
            word=word,
            lemma=self.lemmatize(raw_data),
            weight=raw_data[1],
            raw_tags=("n", "nom"),
            features=ParsingResults([PartOfSpeech.NOUN]),
        )

    def decode_generation(self, data: tuple[str, float]) -> GenerationResult:
        return GenerationResult(word=data[0], weight=data[1])


@pytest.fixture
def morph() -> tuple[FakeMorph, FakeEngine]:
    engine = FakeEngine()
    return TatarMorph(engine, FakeDataDecoder()), engine


def test_parse_normalizes_word_and_preserves_weight(
    morph: tuple[FakeMorph, FakeEngine],
) -> None:
    service, engine = morph

    analysis = next(service.parse("  ӨЙ  "))

    assert engine.analyzed_words == ["өй"]
    assert analysis.word == "өй"
    assert analysis.lemma == "өй"
    assert analysis.weight == 0.25
    assert analysis.raw_tags == ("n", "nom")


def test_generate_normalizes_lemma_and_preserves_results(
    morph: tuple[FakeMorph, FakeEngine],
) -> None:
    service, engine = morph

    assert list(service.generate("  ӨЙ  ", (PartOfSpeech.NOUN,))) == [
        GenerationResult(word="Өй", weight=0.5)
    ]
    assert engine.generated_forms == ["өй<noun>"]


def test_custom_normalizer_is_used() -> None:
    engine = FakeEngine()
    service = TatarMorph(
        engine,
        FakeDataDecoder(),
        normalizer=lambda word: word.strip(),
    )

    next(service.parse("  ӨЙ  "))

    assert engine.analyzed_words == ["ӨЙ"]

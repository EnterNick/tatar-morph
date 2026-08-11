from collections.abc import Iterable

import pytest

from tatar_morph.decoder.interface import EngineData
from tatar_morph.models import ParsingResults, Analysis
from tatar_morph.morph import TatarMorph
from tatar_morph.types import PartOfSpeech


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


class FakeDataParser:
    def parse(self, data: tuple[str, float]) -> EngineData:
        return EngineData(
            word=data[0],
            weight=data[1],
        )

    def parse_list(self, data: Iterable[tuple[str, float]]) -> list[EngineData]:
        return list(map(self.parse, data))

    def lemmatize(self, data: tuple[str, float]) -> str:
        return data[0].split("<", maxsplit=1)[0]

    def parse_features(
        self, data: tuple[str, float]
    ) -> tuple[ParsingResults, tuple[str, ...]]:
        return ParsingResults([PartOfSpeech.NOUN]), ("n", "nom")

    def generate(self, lemma: str, tags: Iterable[str]) -> str:
        tags = tuple(tags)
        if not tags:
            raise ValueError("At least one morphology tag is required")
        return f"{lemma}<{'><'.join(tags)}>"

    def decode(self, word: str, raw_data: tuple[str, float]) -> Analysis:
        return Analysis(
            word=word,
            lemma=self.lemmatize(raw_data),
            weight=raw_data[1],
            raw_tags=("n",),
            features=ParsingResults([PartOfSpeech.NOUN]),
        )


@pytest.fixture
def morph() -> tuple[TatarMorph[tuple[str, float]], FakeEngine]:
    engine = FakeEngine()
    return TatarMorph(engine, FakeDataParser()), engine


def test_parse_normalizes_word_and_preserves_weight(
    morph: tuple[TatarMorph[tuple[str, float]], FakeEngine],
) -> None:
    service, engine = morph

    analysis = next(service.parse("  ӨЙ  "))

    assert engine.analyzed_words == ["өй"]
    assert analysis.word == "өй"
    assert analysis.lemma == "өй"
    assert analysis.weight == 0.25
    assert analysis.raw_tags == ("n", "nom")


def test_generate_normalizes_lemma_and_preserves_results(
    morph: tuple[TatarMorph[tuple[str, float]], FakeEngine],
) -> None:
    service, engine = morph

    assert list(service.generate("  ӨЙ  ", ("n", "nom"))) == [("Өй", 0.5)]
    assert engine.generated_forms == ["өй<n><nom>"]

import pytest

from tatar_morph.decoder.hfst.data import HFSTDataDecoder
from tatar_morph.exceptions import UnsupportedGenerationFeatureError
from tatar_morph.types import (
    Case,
    ComparisonDegree,
    PartOfSpeech,
    PronounType,
    TechnicalTag,
)


@pytest.fixture
def decoder() -> HFSTDataDecoder:
    return HFSTDataDecoder()


def test_parse_extracts_pos_without_duplicating_it_in_features(
    decoder: HFSTDataDecoder,
) -> None:
    features, tags = decoder.parse_features(("өй<n><nom>", 0.0))

    assert features.all() == (PartOfSpeech.NOUN, Case.NOMINATIVE)
    assert tags == ("n", "nom")


def test_parse_preserves_secondary_part_of_speech_as_feature(
    decoder: HFSTDataDecoder,
) -> None:
    features, _ = decoder.parse_features(("өй<n><nom>+и<cop>", 0.0))

    assert features.get_all(PartOfSpeech) == (PartOfSpeech.NOUN, PartOfSpeech.COPULA)


def test_parse_handles_analysis_without_pos(decoder: HFSTDataDecoder) -> None:
    features, tags = decoder.parse_features(("бар<phrase>", 0.0))
    assert features.get_all(TechnicalTag) == (TechnicalTag.PHRASE,)
    assert tags == ("phrase",)


@pytest.mark.parametrize(
    ("lexical_form", "expected_tags"),
    [("бар", ()), ("бар<future_tag>", ("future_tag",))],
)
def test_parse_handles_missing_or_unknown_tags(
    decoder: HFSTDataDecoder,
    lexical_form: str,
    expected_tags: tuple[str, ...],
) -> None:
    features, tags = decoder.parse_features((lexical_form, 0.0))
    assert features.all() == ()
    assert tags == expected_tags


def test_encode_generation_builds_simple_lexical_form(
    decoder: HFSTDataDecoder,
) -> None:
    assert decoder.encode_generation(
        "өй", iter((PartOfSpeech.NOUN, Case.NOMINATIVE))
    ) == "өй<n><nom>"


def test_encode_generation_does_not_depend_on_enum_values(
    decoder: HFSTDataDecoder,
) -> None:
    assert ComparisonDegree.COMPARATIVE.value == "comparative"
    assert decoder.encode_generation(
        "яхшы", (ComparisonDegree.COMPARATIVE,)
    ) == "яхшы<comp>"


def test_encode_generation_rejects_empty_features(decoder: HFSTDataDecoder) -> None:
    with pytest.raises(ValueError, match="At least one morphology feature"):
        decoder.encode_generation("өй", [])


def test_encode_generation_rejects_unsupported_feature(
    decoder: HFSTDataDecoder,
) -> None:
    with pytest.raises(UnsupportedGenerationFeatureError, match="HFST cannot encode"):
        decoder.encode_generation("өй", (PronounType.NEGATIVE,))

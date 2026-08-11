import pytest

from tatar_morph.tags.hfst.tags import HFSTTagsParser
from tatar_morph.types import Case, PartOfSpeech, TechnicalTag


@pytest.fixture
def parser() -> HFSTTagsParser:
    return HFSTTagsParser()


def test_parse_extracts_pos_without_duplicating_it_in_features(
    parser: HFSTTagsParser,
) -> None:
    features, tags = parser.parse(("өй<n><nom>", 0.0))

    assert features.list() == [PartOfSpeech.NOUN, Case.NOMINATIVE]
    assert tags == ("n", "nom")


def test_parse_preserves_secondary_part_of_speech_as_feature(
    parser: HFSTTagsParser,
) -> None:
    features, _ = parser.parse(("өй<n><nom>+и<cop>", 0.0))

    assert features.get_all(PartOfSpeech) == (PartOfSpeech.NOUN, PartOfSpeech.COPULA)


def test_parse_handles_analysis_without_pos(parser: HFSTTagsParser) -> None:
    features, tags = parser.parse(("бар<phrase>", 0.0))
    assert features.get_all(TechnicalTag) is TechnicalTag.PHRASE
    assert tags == ("phrase",)


@pytest.mark.parametrize(
    ("lexical_form", "expected_tags"),
    [("бар", ()), ("бар<future_tag>", ("future_tag",))],
)
def test_parse_handles_missing_or_unknown_tags(
    parser: HFSTTagsParser,
    lexical_form: str,
    expected_tags: tuple[str, ...],
) -> None:
    features, tags = parser.parse((lexical_form, 0.0))
    assert features.list() == []
    assert tags == expected_tags


def test_resolve_builds_simple_lexical_form(parser: HFSTTagsParser) -> None:
    assert parser.resolve("өй", iter(("n", "nom"))) == "өй<n><nom>"


def test_resolve_rejects_empty_tags(parser: HFSTTagsParser) -> None:
    with pytest.raises(ValueError, match="At least one morphology tag"):
        parser.resolve("өй", [])

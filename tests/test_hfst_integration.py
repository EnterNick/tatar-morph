from pathlib import Path

import pytest

from tatar_morph import HFSTMorph, TransducerLoadError, build_default_hfst_morph
from tatar_morph.engines.hfst_engine import HfstEngine
from tatar_morph.types import TechnicalTag

RESOURCE_DIR = Path(__file__).parents[1] / "resources"


def build_morph() -> HFSTMorph:
    return build_default_hfst_morph(
        RESOURCE_DIR / "tat.automorf.hfst",
        RESOURCE_DIR / "tat.autogen.hfst",
    )


def test_parse_bar_includes_phrase_without_aborting() -> None:
    analyses = list(build_morph().parse("бар"))
    phrase = next(item for item in analyses if item.raw_tags == ("phrase",))

    assert phrase.features.get_all(TechnicalTag) == (TechnicalTag.PHRASE,)


def test_simple_analysis_tags_can_be_generated() -> None:
    morph = build_morph()
    analysis = next(item for item in morph.parse("өй") if item.raw_tags == ("n", "nom"))

    assert list(morph.generate(analysis.lemma, analysis.raw_tags)) == [("өй", 0.0)]


def test_missing_transducer_error_contains_role_and_path(tmp_path: Path) -> None:
    missing_path = tmp_path / "missing.hfst"

    with pytest.raises(TransducerLoadError, match=r"analyzer.*missing\.hfst"):
        HfstEngine(missing_path, RESOURCE_DIR / "tat.autogen.hfst")


def test_invalid_transducer_error_preserves_cause(tmp_path: Path) -> None:
    invalid_path = tmp_path / "invalid.hfst"
    invalid_path.write_text("not a transducer")

    with pytest.raises(TransducerLoadError, match=r"analyzer.*invalid\.hfst") as error:
        HfstEngine(invalid_path, RESOURCE_DIR / "tat.autogen.hfst")

    assert error.value.__cause__ is not None

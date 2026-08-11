from pathlib import Path

from tatar_morph.decoder.hfst.data import HFSTDataDecoder
from tatar_morph.engines.hfst_engine import HfstEngine
from tatar_morph.morph import TatarMorph
from tatar_morph.types import TechnicalTag

RESOURCE_DIR = Path(__file__).parents[1] / "resources"


def build_morph() -> TatarMorph[tuple[str, float]]:
    return TatarMorph(
        HfstEngine(
            RESOURCE_DIR / "tat.automorf.hfst",
            RESOURCE_DIR / "tat.autogen.hfst",
        ),
        HFSTDataDecoder(),
    )


def test_parse_bar_includes_phrase_without_aborting() -> None:
    analyses = list(build_morph().parse("бар"))
    phrase = next(item for item in analyses if item.raw_tags == ("phrase",))

    assert phrase.features.get_all(TechnicalTag) is TechnicalTag.PHRASE


def test_simple_analysis_tags_can_be_generated() -> None:
    morph = build_morph()
    analysis = next(item for item in morph.parse("өй") if item.raw_tags == ("n", "nom"))

    assert list(morph.generate(analysis.lemma, analysis.raw_tags)) == [("өй", 0.0)]

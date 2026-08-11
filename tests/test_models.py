from tatar_morph.models import Analysis, ParsingResults
from tatar_morph.types import Case, Number, PartOfSpeech


def test_parsing_results_gets_feature_by_exact_type() -> None:
    results = ParsingResults([Number.PLURAL, Case.NOMINATIVE])

    assert results.get_all(Number) is Number.PLURAL
    assert results.get_all(Case) is Case.NOMINATIVE
    assert results.get_all(PartOfSpeech) is None


def test_analysis_uses_immutable_tags_and_allows_missing_pos() -> None:
    analysis = Analysis(
        word="бар",
        lemma="бар",
        features=ParsingResults([]),
        weight=0.0,
        raw_tags=("phrase",),
    )

    assert analysis.raw_tags == ("phrase",)

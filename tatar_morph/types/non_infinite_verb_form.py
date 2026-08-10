from enum import StrEnum


class NonFiniteVerbForm(StrEnum):
    PERFECT_PARTICIPLE = "perfect_participle"
    IMPERFECT_PARTICIPLE = "imperfect_participle"
    VOLITIONAL_PARTICIPLE = "volitional_participle"
    CONDITIONAL_PARTICIPLE = "conditional_participle"
    PLANNED_FUTURE_PARTICIPLE = "planned_future_participle"

    PERFECT_CONVERB = "perfect_converb"
    CONDITIONAL_CONVERB = "conditional_converb"
    UNTIL_CONVERB = "until_converb"
    AFTER_CONVERB = "after_converb"
    NEGATIVE_CONVERB = "negative_converb"

    PAST_VERBAL_ADJECTIVE = "past_verbal_adjective"
    IMPERFECT_VERBAL_ADJECTIVE = "imperfect_verbal_adjective"
    POTENTIAL_VERBAL_ADJECTIVE = "potential_verbal_adjective"
    ABILITY_VERBAL_ADJECTIVE = "ability_verbal_adjective"

    INDEFINITE_FUTURE_VERBAL_ADJECTIVE = "indefinite_future_verbal_adjective"
    DEFINITE_FUTURE_VERBAL_ADJECTIVE = "definite_future_verbal_adjective"
    PROSPECTIVE_VERBAL_ADJECTIVE = "prospective_verbal_adjective"

    VERBAL_NOUN = "verbal_noun"
    PAST_VERBAL_NOUN = "past_verbal_noun"
    PERFECT_VERBAL_NOUN = "perfect_verbal_noun"
    ABILITY_VERBAL_NOUN = "ability_verbal_noun"

    INDEFINITE_FUTURE_VERBAL_NOUN = "indefinite_future_verbal_noun"
    DEFINITE_FUTURE_VERBAL_NOUN = "definite_future_verbal_noun"
    PROSPECTIVE_VERBAL_NOUN = "prospective_verbal_noun"

    MAK_VERBAL_NOUN = "mak_verbal_noun"
    ABSTRACT_VERBAL_NOUN = "abstract_verbal_noun"

    INFINITIVE = "infinitive"

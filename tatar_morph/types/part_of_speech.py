from enum import StrEnum


class PartOfSpeech(StrEnum):
    NOUN = "noun"
    PROPER_NOUN = "proper_noun"
    ADJECTIVE = "adjective"
    NUMERAL = "numeral"
    PRONOUN = "pronoun"
    DETERMINER = "determiner"

    VERB = "verb"
    AUXILIARY_VERB = "auxiliary_verb"
    COPULA = "copula"

    ADVERB = "adverb"
    POSTPOSITION = "postposition"
    POSTADVERB = "postadverb"

    COORDINATING_CONJUNCTION = "coordinating_conjunction"
    SUBORDINATING_CONJUNCTION = "subordinating_conjunction"
    ADVERBIAL_CONJUNCTION = "adverbial_conjunction"

    INTERJECTION = "interjection"
    IDEOPHONE = "ideophone"
    ABBREVIATION = "abbreviation"

    LETTER = "letter"
    PUNCTUATION = "punctuation"

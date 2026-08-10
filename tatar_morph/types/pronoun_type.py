from enum import StrEnum


class PronounType(StrEnum):
    PERSONAL = "personal"
    RECIPROCAL = "reciprocal"
    DEMONSTRATIVE = "demonstrative"
    INDEFINITE = "indefinite"
    INTERROGATIVE = "interrogative"
    QUANTIFIER = "quantifier"
    NEGATIVE = "negative"
    REFLEXIVE = "reflexive"

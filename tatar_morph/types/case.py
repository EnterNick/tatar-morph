from enum import StrEnum


class Case(StrEnum):
    NOMINATIVE = "nom"
    GENITIVE = "gen"
    DATIVE = "dat"
    ACCUSATIVE = "acc"
    LOCATIVE = "loc"
    ABLATIVE = "abl"

    SIMILATIVE = "sim"
    ABESSIVE = "abe"
    REASON = "reas"
    EQUATIVE = "equ"

from enum import StrEnum


class Possessive(StrEnum):
    GENERAL = "general"

    FIRST_SINGULAR = "first_singular"
    SECOND_SINGULAR = "second_singular"
    THIRD_SINGULAR_OR_PLURAL = "third_singular_or_plural"

    FIRST_PLURAL = "first_plural"
    SECOND_PLURAL = "second_plural"
    THIRD_PLURAL = "third_plural"

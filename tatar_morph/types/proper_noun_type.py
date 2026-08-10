from enum import StrEnum


class ProperNounType(StrEnum):
    TOPONYM = "toponym"
    ANTHROPONYM = "anthroponym"
    COGNOMEN = "cognomen"
    PATRONYMIC = "patronymic"
    ORGANIZATION = "organization"
    OTHER = "other"
    UNKNOWN = "unknown"

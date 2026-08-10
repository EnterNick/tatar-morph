from enum import StrEnum


class PunctuationType(StrEnum):
    SENTENCE_MARKER = "sentence_marker"

    HYPHEN = "hyphen"
    COMMA = "comma"
    APOSTROPHE = "apostrophe"

    QUOTE = "quote"
    LEFT_QUOTE = "left_quote"
    RIGHT_QUOTE = "right_quote"

    LEFT_PARENTHESIS = "left_parenthesis"
    RIGHT_PARENTHESIS = "right_parenthesis"

    ASTERISK = "asterisk"
    COMMERCIAL_AT = "commercial_at"
    TILDE = "tilde"
    LOW_LINE = "low_line"
    VERTICAL_LINE = "vertical_line"

    EURO_SIGN = "euro_sign"
    DOLLAR_SIGN = "dollar_sign"
    POUND_SIGN = "pound_sign"
    YEN_SIGN = "yen_sign"
    PERCENT_SIGN = "percent_sign"

    SECTION_SIGN = "section_sign"
    COPYRIGHT_SIGN = "copyright_sign"
    REGISTERED_SIGN = "registered_sign"
    PILCROW = "pilcrow"

    INVERTED_QUESTION_MARK = "inverted_question_mark"
    MULTIPLICATION_SIGN = "multiplication_sign"
    DIVISION_SIGN = "division_sign"

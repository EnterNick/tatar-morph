from tatar_morph.types.case import Case
from tatar_morph.types.comparison_degree import ComparisonDegree
from tatar_morph.types.formality import Formality
from tatar_morph.types.gender import Gender
from tatar_morph.types.modal_particle_type import ModalParticleType
from tatar_morph.types.mood import Mood
from tatar_morph.types.non_infinite_verb_form import NonFiniteVerbForm
from tatar_morph.types.number import Number
from tatar_morph.types.numeral_type import NumeralType
from tatar_morph.types.part_of_speech import PartOfSpeech
from tatar_morph.types.person import Person
from tatar_morph.types.polarity import Polarity
from tatar_morph.types.possessive import Possessive
from tatar_morph.types.pronoun_type import PronounType
from tatar_morph.types.proper_noun_type import ProperNounType
from tatar_morph.types.punctuation_type import PunctuationType
from tatar_morph.types.technical_tag import TechnicalTag
from tatar_morph.types.tense import Tense
from tatar_morph.types.transitivity import Transitivity
from tatar_morph.types.usage import Usage
from tatar_morph.types.voice import Voice

type AnyType = (
    Case
    | Number
    | PartOfSpeech
    | Possessive
    | PronounType
    | NumeralType
    | Transitivity
    | Voice
    | Mood
    | Tense
    | Usage
    | NonFiniteVerbForm
    | Person
    | Gender
    | ProperNounType
    | ComparisonDegree
    | Formality
    | Polarity
    | ModalParticleType
    | PunctuationType
    | TechnicalTag
)


__all__ = [
    "Case",
    "ComparisonDegree",
    "Formality",
    "Gender",
    "ModalParticleType",
    "Mood",
    "NonFiniteVerbForm",
    "Number",
    "NumeralType",
    "PartOfSpeech",
    "Person",
    "Polarity",
    "Possessive",
    "PronounType",
    "ProperNounType",
    "PunctuationType",
    "TechnicalTag",
    "Tense",
    "Transitivity",
    "Usage",
    "Voice",
    "AnyType",
]

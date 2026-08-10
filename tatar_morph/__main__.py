from os import getenv
from pathlib import Path

from tatar_morph.engines.hfst_engine import HfstEngine
from tatar_morph.lemma import HFSTLemmatizer
from tatar_morph.morph import TatarMorph
from tatar_morph.tags import HFSTTagsParser

def parse_env_path(name: str) -> Path:
    env_path = getenv(name)
    if not env_path:
        raise EnvironmentError(f"Environment variable {name} not found")
    return Path(env_path)

def build_default_hfst_morph() -> TatarMorph:
    automorf_path = parse_env_path("TATAR_AUTOMORF_PATH")
    autogen_path = parse_env_path("TATAR_AUTOGEN_PATH")

    engine = HfstEngine(
        analyzer_path=automorf_path,
        generator_path=autogen_path,
    )

    tags_mapper = HFSTTagsParser()
    lemma_parser = HFSTLemmatizer()
    return TatarMorph(
        tags_parser=tags_mapper,
        lemma_parser=lemma_parser,
        engine=engine,
    )

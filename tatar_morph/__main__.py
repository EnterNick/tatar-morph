from os import getenv
from pathlib import Path

from tatar_morph.decoder.hfst.data import HFSTDataDecoder
from tatar_morph.engines.hfst_engine import HfstEngine
from tatar_morph.morph import TatarMorph


def parse_env_path(name: str) -> Path:
    env_path = getenv(name)
    if not env_path:
        raise OSError(f"Environment variable {name} not found")
    return Path(env_path)


def build_default_hfst_morph(
    automorf_path: Path | None = None, autogen_path: Path | None = None
) -> TatarMorph[tuple[str, float]]:
    if automorf_path is None:
        automorf_path = parse_env_path("TATAR_AUTOMORF_PATH")
    if autogen_path is None:
        autogen_path = parse_env_path("TATAR_AUTOGEN_PATH")

    engine = HfstEngine(
        analyzer_path=automorf_path,
        generator_path=autogen_path,
    )

    return TatarMorph(
        data_decoder=HFSTDataDecoder(),
        engine=engine,
    )

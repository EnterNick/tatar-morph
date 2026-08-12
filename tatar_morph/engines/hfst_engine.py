from collections.abc import Iterable
from pathlib import Path

import hfst


class TransducerLoadError(RuntimeError):
    """Raised when an HFST transducer cannot be loaded."""


class HfstEngine:
    def __init__(
        self,
        analyzer_path: Path,
        generator_path: Path,
    ) -> None:
        self._analyzer = self._load(analyzer_path, purpose="analyzer")
        self._generator = self._load(generator_path, purpose="generator")

    @staticmethod
    def _load(path: Path, *, purpose: str) -> hfst.HfstTransducer:
        if not path.is_file():
            raise TransducerLoadError(f"HFST {purpose} file does not exist: {path}")

        try:
            stream = hfst.HfstInputStream(str(path))
            try:
                return stream.read()
            finally:
                stream.close()
        except Exception as error:
            raise TransducerLoadError(
                f"Failed to load HFST {purpose} from {path}"
            ) from error

    def analyze(self, word: str) -> Iterable[tuple[str, float]]:
        return self._analyzer.lookup(word)

    def generate(self, lexical_form: str) -> Iterable[tuple[str, float]]:
        return self._generator.lookup(lexical_form)

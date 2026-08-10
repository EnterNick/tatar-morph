from pathlib import Path

import hfst


class HfstEngine:
    def __init__(
        self,
        analyzer_path: Path,
        generator_path: Path,
    ) -> None:
        self._analyzer = self._load(analyzer_path)
        self._generator = self._load(generator_path)

    @staticmethod
    def _load(path: Path) -> hfst.HfstTransducer:
        stream = hfst.HfstInputStream(str(path))

        try:
            return stream.read()
        finally:
            stream.close()

    def analyze(self, word: str) -> list[tuple[str, float]]:
        return list(self._analyzer.lookup(word))

    def generate(self, lexical_form: str) -> list[tuple[str, float]]:
        return list(self._generator.lookup(lexical_form))

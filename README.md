# tatar-morph

`tatar-morph` is a Python library for morphological analysis, lemmatization,
and word-form generation for the Tatar language. It uses the
[`hfst`](https://pypi.org/project/hfst/) package to work with HFST transducers.

> The project is at an early stage of development. The public API may change
> between releases.

## Features

- Parse a word into its lemma and morphological features.
- Return all possible lemmas for a word.
- Generate word forms from a lemma and a set of features.
- Represent parts of speech, cases, numbers, tenses, and other grammatical
  categories with typed values.
- Work with existing HFST analyzer and generator transducers.

## Requirements

- Python 3.12 or newer.
- An HFST transducer for analyzing Tatar words.
- An HFST transducer for generating Tatar word forms.

The transducers are not bundled with the package and must be obtained separately.

## Installation

```bash
python -m pip install tatar-morph
```

## Quick start

You can pass the transducer paths directly:

```python
from pathlib import Path

from tatar_morph import build_default_hfst_morph

morph = build_default_hfst_morph(
    automorf_path=Path("/path/to/tat.automorf.hfst"),
    autogen_path=Path("/path/to/tat.autogen.hfst"),
)

for analysis in morph.parse("өй"):
    print(analysis.lemma)
    print(analysis.features.all())
    print(analysis.raw_tags)

print(morph.lemmatize("өйләр"))
```

Alternatively, set the `TATAR_AUTOMORF_PATH` and `TATAR_AUTOGEN_PATH`
environment variables:

```bash
export TATAR_AUTOMORF_PATH=/path/to/tat.automorf.hfst
export TATAR_AUTOGEN_PATH=/path/to/tat.autogen.hfst
```

```python
from tatar_morph import build_default_hfst_morph

morph = build_default_hfst_morph()
analyses = list(morph.parse("бар"))
```

Features returned by the analyzer can be used to generate word forms:

```python
analysis = next(morph.parse("өй"))
forms = list(morph.generate(analysis.lemma, analysis.features.all()))

for form in forms:
    print(form.word, form.weight)
```

## Development

Install the dependencies and run the checks:

```bash
uv sync --dev
uv run pytest
uv run ruff check .
uv run mypy tatar_morph
```

## Releasing a new version

The package version is derived automatically from the Git tag by
`setuptools-scm`. Create a tag prefixed with `v` and push it to GitHub:

```bash
git tag v0.1.0
git push origin v0.1.0
```

GitHub Actions derives the version from the tag, verifies the version in the
built wheel, publishes the package to PyPI, and creates a GitHub Release.
Before the first release, configure a Trusted Publisher for the `tatar-morph`
project on PyPI with the `EnterNick/tatar-morph` repository, the `release.yml`
workflow, and the `pypi` environment.

## License

This project is distributed under the GNU General Public License version 3.
See [`LICENSE`](LICENSE) for the full license text.

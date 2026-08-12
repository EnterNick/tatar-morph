# tatar-morph

`tatar-morph` — библиотека на Python для морфологического анализа,
лемматизации и генерации словоформ татарского языка. Для работы с
HFST-трансдьюсерами библиотека использует пакет [`hfst`](https://pypi.org/project/hfst/).

> Проект находится на ранней стадии разработки. Публичный API может меняться
> между версиями.

## Возможности

- разбор слова на лемму и морфологические признаки;
- получение списка возможных лемм;
- генерация словоформ по лемме и набору признаков;
- типизированное представление частей речи, падежей, числа, времени и других
  грамматических категорий;
- работа с готовыми анализирующим и генерирующим HFST-трансдьюсерами.

## Требования

- Python 3.12 или новее;
- HFST-трансдьюсер для анализа татарского языка;
- HFST-трансдьюсер для генерации словоформ.

Трансдьюсеры не входят в пакет и должны быть получены отдельно.

## Установка

```bash
python -m pip install tatar-morph
```

## Быстрый старт

Пути к трансдьюсерам можно передать напрямую:

```python
from pathlib import Path

from tatar_morph import build_default_hfst_morph

morph = build_default_hfst_morph(
    automorf_path=Path("/путь/к/tat.automorf.hfst"),
    autogen_path=Path("/путь/к/tat.autogen.hfst"),
)

for analysis in morph.parse("өй"):
    print(analysis.lemma)
    print(analysis.features.all())
    print(analysis.raw_tags)

print(morph.lemmatize("өйләр"))
```

Или задать их переменными окружения `TATAR_AUTOMORF_PATH` и
`TATAR_AUTOGEN_PATH`:

```bash
export TATAR_AUTOMORF_PATH=/путь/к/tat.automorf.hfst
export TATAR_AUTOGEN_PATH=/путь/к/tat.autogen.hfst
```

```python
from tatar_morph import build_default_hfst_morph

morph = build_default_hfst_morph()
analyses = list(morph.parse("бар"))
```

Для генерации можно использовать признаки, полученные при разборе:

```python
analysis = next(morph.parse("өй"))
forms = list(morph.generate(analysis.lemma, analysis.features.all()))

for form in forms:
    print(form.word, form.weight)
```

## Разработка

Установите зависимости и запустите проверки:

```bash
uv sync --dev
uv run pytest
uv run ruff check .
uv run mypy tatar_morph
```

## Выпуск новой версии

Версия пакета определяется автоматически из Git-тега с помощью
`setuptools-scm`. Создайте тег с префиксом `v` и отправьте его в GitHub:

```bash
git tag v0.1.0
git push origin v0.1.0
```

GitHub Actions получит версию из тега, проверит версию собранного wheel,
опубликует пакет в PyPI и создаст GitHub Release. Для публикации необходимо
однократно настроить Trusted Publisher проекта `tatar-morph` в PyPI для
репозитория `EnterNick/tatar-morph`, workflow `release.yml` и окружения `pypi`.

## Лицензия

Проект распространяется на условиях GNU General Public License версии 3.
Полный текст лицензии находится в файле [`LICENSE`](LICENSE).

import re

_whitespace_re = re.compile(r"\s+")
_url_re = re.compile(r"https?://\S+")
_html_re = re.compile(r"<[^>]+>")

def clean_text(text: str) -> str:
    """
    Минимальная очистка текста писем:
    - удаляем html-теги и url
    - оставляем буквы/цифры и пробел
    - схлопываем пробелы, приводим к нижнему регистру
    """
    if text is None:
        return ""
    x = str(text)
    x = _html_re.sub(" ", x)
    x = _url_re.sub(" ", x)
    x = re.sub(r"[^0-9a-zA-Zа-яА-ЯёЁ ]+", " ", x)
    x = _whitespace_re.sub(" ", x).strip().lower()
    return x

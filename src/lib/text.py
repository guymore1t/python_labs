import re


def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    if yo2e:
        text = text.replace('Ё', 'E')
        text = text.replace('ё', 'е')

    text = text.replace('\r', ' ').replace('\t', ' ').replace('\n', ' ')
    text = text.split()
    text = ' '.join(text)

    if casefold:
        text = text.casefold()

    return text


def tokenize(text: str) -> list[str]:
    pattern = r'\w+(?:-\w+)*'
    return re.findall(pattern, text)


def count_freq(tokens: list[str]) -> dict[str, int]:
    freq: dict[str, int] = {}
    for token in tokens:
        freq[token] = freq.get(token, 0) + 1
    return freq


def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    items = list(freq.items())
    items.sort(key=lambda item: (-item[1], item[0]))
    return items[:n]

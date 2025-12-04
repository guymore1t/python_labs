import argparse
import sys
from pathlib import Path

current_file = Path(__file__)
parent_dir = current_file.parent.parent
sys.path.insert(0, str(parent_dir))

from lib.text import normalize, tokenize, count_freq, top_n


def main():
    parser = argparse.ArgumentParser(
        description="CLI утилиты для текста", add_help=False
    )

    subparsers = parser.add_subparsers(dest="command", title="доступные команды")

    cat_parser = subparsers.add_parser("cat", help="Показать содержимое файла")
    cat_parser.add_argument("--input", required=True, help="Входной файл")
    cat_parser.add_argument("-n", action="store_true", help="Показать номера строк")

    stats_parser = subparsers.add_parser("stats", help="Статистика по тексту")
    stats_parser.add_argument("--input", required=True, help="Входной файл")
    stats_parser.add_argument("--top", type=int, default=5, help="Количество топ-слов")

    parser.add_argument(
        "-h",
        "--help",
        action="help",
        default=argparse.SUPPRESS,
        help="Показать справку",
    )

    args = parser.parse_args()

    if args.command is None:
        return

    if args.command == "cat":
        path = Path(args.input)
        if not path.exists():
            print(f"Ошибка: Файл не найден: {path}")
            sys.exit(1)

        try:
            with open(path, "r", encoding="utf-8") as f:
                lines = f.readlines()
        except Exception as e:
            print(f"Ошибка при чтении файла: {e}")
            sys.exit(1)

        for i, line in enumerate(lines, 1):
            if args.n:
                print(f"{i:6d}  {line}", end="")
            else:
                print(line, end="")

    elif args.command == "stats":
        path = Path(args.input)
        if not path.exists():
            print(f"Ошибка: Файл не найден: {path}")
            sys.exit(1)

        try:
            with open(path, "r", encoding="utf-8") as f:
                text = f.read()
        except Exception as e:
            print(f"Ошибка при чтении файла: {e}")
            sys.exit(1)

        text = normalize(text)
        tokens = tokenize(text)
        freq = count_freq(tokens)
        top_words = top_n(freq, args.top)

        print(f"Всего слов: {len(tokens)}")
        print(f"Уникальных слов: {len(freq)}")
        print(f"Топ-{args.top}:")
        for word, cnt in top_words:
            print(f"  {word}: {cnt}")


if __name__ == "__main__":
    main()

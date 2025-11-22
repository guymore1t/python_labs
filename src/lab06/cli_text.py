import argparse
import sys
from pathlib import Path

current_file = Path(__file__)
src_dir = current_file.parent.parent
sys.path.insert(0, str(src_dir))

from lib.text import normalize, tokenize, count_freq, top_n



def stats_command(args):
    input_path = Path(args.input)

    if not input_path.exists():
        raise FileNotFoundError(f"Файл не найден: {input_path}")

    try:
        with open(input_path, "r", encoding="utf-8") as f:
            text = f.read()
    except Exception as e:
        raise FileNotFoundError(f"Ошибка при чтении файла: {e}")

    text = normalize(text)
    tokens = tokenize(text)

    freq_dict = {}
    for token in tokens:
        freq_dict[token] = freq_dict.get(token, 0) + 1

    top_words = top_n(freq_dict, args.top)

    print(f"Всего слов: {len(tokens)}")
    print(f"Уникальных слов: {len(freq_dict)}")
    print(f"Топ-{args.top}:")
    for word, count in top_words:
        print(f"  {word}: {count}")


def cat_command(args):
    input_path = Path(args.input)

    if not input_path.exists():
        raise FileNotFoundError(f"Файл не найден: {input_path}")

    try:
        with open(input_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except Exception as e:
        raise FileNotFoundError(f"Ошибка при чтении файла: {e}")

    for i, line in enumerate(lines, start=1):
        if args.n:
            print(f"{i:6d}  {line}", end="")
        else:
            print(line, end="")


def main():
    parser = argparse.ArgumentParser(
        description="CLI модуль для работы с текстом"
    )

    subparsers = parser.add_subparsers(dest="command")

    stats_parser = subparsers.add_parser("stats", help="Анализ частот слов")
    stats_parser.add_argument("--input", required=True)
    stats_parser.add_argument("--top", type=int, default=5)

    cat_parser = subparsers.add_parser("cat", help="Вывод содержимого файла")
    cat_parser.add_argument("--input", required=True)
    cat_parser.add_argument("-n", action="store_true")

    args = parser.parse_args()

    if not args.command:
        parser.error("Необходимо указать команду (stats или cat)")

    try:
        if args.command == "stats":
            stats_command(args)
        elif args.command == "cat":
            cat_command(args)
    except FileNotFoundError as e:
        parser.error(str(e))
    except Exception as e:
        parser.error(f"Ошибка: {e}")


if __name__ == "__main__":
    main()

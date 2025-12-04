from pathlib import Path
import sys

current_dir = Path(__file__).parent
lib_path = current_dir.parent / "lib"
sys.path.append(str(lib_path))

from text import normalize, tokenize, count_freq

INPUT_FILE = "data/lab04/input.txt"
OUTPUT_FILE = "data/lab04/report.csv"
ENCODING = "utf-8"


def main():
    if not Path(INPUT_FILE).exists():
        print(f"Ошибка: файл {INPUT_FILE} не найден!")
        print("Создайте файл data/lab04/input.txt с текстом")
        sys.exit(1)

    try:
        with open(INPUT_FILE, "r", encoding=ENCODING) as f:
            text = f.read()

    except:
        print("Ошибка при чтении файла!")
        sys.exit(1)

    total_words = 0
    unique_words = 0
    word_counts = []

    if not text.strip():
        Path(OUTPUT_FILE).parent.mkdir(exist_ok=True)
        with open(OUTPUT_FILE, "w", encoding=ENCODING) as f:
            f.write("word,count\n")

    if text.strip():
        clean_text = normalize(text)
        words = tokenize(clean_text)
        word_counts = count_freq(words)

        total_words = len(words)
        unique_words = len(word_counts)

        Path(OUTPUT_FILE).parent.mkdir(exist_ok=True)

        with open(OUTPUT_FILE, "w", encoding=ENCODING) as f:
            f.write("word,count\n")
            for word, count in word_counts:
                f.write(f"{word},{count}\n")

    print(f"Всего слов: {total_words}")
    print(f"Уникальных слов: {unique_words}")
    print("Топ-5:")
    for word, count in word_counts[:5]:
        print(f"{word}:{count}")


if __name__ == "__main__":
    main()

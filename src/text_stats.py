import sys
from lib import text

input_text = sys.stdin.readline()

normalized_text = text.normalize(input_text, casefold=True, yo2e=True)
tokens = text.tokenize(normalized_text)
freq = text.count_freq(tokens)

words_count = len(tokens)
unique_words = len(freq)
top_5 = freq[:5]

print(f"Всего слов: {words_count}")
print(f"Уникальных слов: {unique_words}")
print("Топ-5:")

for word, count in top_5:
    print(f"{word}:{count}")

import json
import csv
from pathlib import Path


def json_to_csv(json_path: str, csv_path: str) -> None:
    if not json_path.lower().endswith('.json'):
        raise ValueError('Входной файл должен иметь расширение .json')
    if not csv_path.lower().endswith('.csv'):
        raise ValueError('Выходной файл должен иметь расширение .csv')

    json_file = Path(json_path)
    csv_file = Path(csv_path)

    if not json_file.exists():
        raise FileNotFoundError('Файл не найден')

    with json_file.open('r', encoding='utf-8') as f:
        content = f.read().strip()
        if not content:
            raise ValueError('JSON-файл пустой')

        try:
            data = json.loads(content)
        except json.JSONDecodeError:
            raise ValueError('Некорректный формат JSON')

    if not isinstance(data, list) or not all(isinstance(x, dict) for x in data):
        raise ValueError('Ожидался список словарей в JSON')
    if not data:
        raise ValueError('JSON файл содержит пустой список')

    headers = list(data[0].keys())
    rows = [{key: obj.get(key, '') for key in headers} for obj in data]

    with csv_file.open('w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(rows)

    if csv_file.stat().st_size == 0:
        raise ValueError("CSV-файл получился пустым")


#if __name__ == "__main__":
    #json_to_csv("data/samples/people.json", "data/out/result1.csv")
    
def csv_to_json(csv_path: str, json_path: str) -> None:

    if not csv_path.lower().endswith('.csv'):
        raise ValueError('Входной файл должен иметь расширение .csv')
    if not json_path.lower().endswith('.json'):
        raise ValueError('Выходной файл должен иметь расширение .json')

    csv_file = Path(csv_path)
    json_file = Path(json_path)

    if not csv_file.exists():
        raise FileNotFoundError("CSV-файл не найден")

    with csv_file.open('r', encoding='utf-8') as f:
        content = f.read().strip()
        if not content:
            raise ValueError("CSV-файл пустой")

    # читаем CSV корректно
    with csv_file.open('r', encoding='utf-8') as f:
        reader = csv.DictReader(f)

        if reader.fieldnames is None:
            raise ValueError("CSV-файл не содержит заголовка")

        rows = list(reader)

    if not rows:
        raise ValueError("CSV-файл не содержит данных")

    original_count = len(rows)

    with json_file.open('w', encoding='utf-8') as f:
        json.dump(rows, f, ensure_ascii=False, indent=2)

    with json_file.open('r', encoding='utf-8') as f:
        try:
            loaded = json.load(f)
        except json.JSONDecodeError:
            raise ValueError("Пустой JSON или некорректная структура")

    if not isinstance(loaded, list):
        raise ValueError("JSON должен содержать список")

    if not all(isinstance(x, dict) for x in loaded):
        raise ValueError("JSON должен содержать список словарей")

    if len(loaded) != original_count:
        raise ValueError("Количество записей не совпадает после конвертации")



if __name__ == "__main__":
    csv_to_json("data/samples/people.csv", "data/out/result2.json")



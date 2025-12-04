import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

import pytest
import json
import csv
from pathlib import Path
from lab05.json_csv import json_to_csv, csv_to_json


def test_json_to_csv_basic(tmp_path):
    """Тест базовой конвертации JSON -> CSV"""
    json_file = tmp_path / "test.json"
    json_data = [
        {"name": "Иван", "age": 25, "city": "Москва"},
        {"name": "Петр", "age": 30, "city": "СПб"},
    ]
    json_file.write_text(json.dumps(json_data, ensure_ascii=False), encoding="utf-8")

    csv_file = tmp_path / "test.csv"

    json_to_csv(str(json_file), str(csv_file))


    assert csv_file.exists()

    with open(csv_file, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    assert len(rows) == 2
    assert rows[0]["name"] == "Иван"
    assert rows[0]["age"] == "25"
    assert rows[0]["city"] == "Москва"
    assert rows[1]["name"] == "Петр"
    assert rows[1]["city"] == "СПб"


def test_json_to_csv_empty_list(tmp_path):
    """Тест с пустым списком в JSON"""
    json_file = tmp_path / "test.json"
    json_file.write_text("[]", encoding="utf-8")

    csv_file = tmp_path / "test.csv"

    with pytest.raises(ValueError, match="JSON файл содержит пустой список"):
        json_to_csv(str(json_file), str(csv_file))


def test_json_to_csv_invalid_json(tmp_path):
    """Тест с некорректным JSON"""
    json_file = tmp_path / "test.json"
    json_file.write_text("{ невалидный json }", encoding="utf-8")

    csv_file = tmp_path / "test.csv"

    with pytest.raises(ValueError, match="Некорректный формат JSON"):
        json_to_csv(str(json_file), str(csv_file))


def test_json_to_csv_file_not_found():
    """Тест с несуществующим файлом"""
    with pytest.raises(FileNotFoundError, match="Файл не найден"):
        json_to_csv("nonexistent.json", "output.csv")


def test_json_to_csv_wrong_extension():
    """Тест с неправильным расширением файла"""
    with pytest.raises(ValueError, match="Входной файл должен иметь расширение .json"):
        json_to_csv("file.txt", "output.csv")


def test_json_to_csv_with_different_keys(tmp_path):
    """Тест с разными наборами ключей в объектах - функция берет ключи только из первого объекта"""
    json_file = tmp_path / "test.json"
    json_data = [
        {"name": "Иван", "age": 25},
        {"name": "Петр", "city": "СПб", "age": 30},
    ]
    json_file.write_text(json.dumps(json_data, ensure_ascii=False), encoding="utf-8")

    csv_file = tmp_path / "test.csv"

    json_to_csv(str(json_file), str(csv_file))

    with open(csv_file, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    assert set(rows[0].keys()) == {"name", "age"}
    assert rows[0]["name"] == "Иван"
    assert rows[0]["age"] == "25"
    assert rows[1]["name"] == "Петр"
    assert rows[1]["age"] == "30"


def test_csv_to_json_basic(tmp_path):
    """Тест базовой конвертации CSV -> JSON"""
    csv_file = tmp_path / "test.csv"
    csv_content = """name,age,city
Иван,25,Москва
Петр,30,СПб"""
    csv_file.write_text(csv_content, encoding="utf-8")

    json_file = tmp_path / "test.json"

    csv_to_json(str(csv_file), str(json_file))

    assert json_file.exists()

    with open(json_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    assert len(data) == 2
    assert data[0]["name"] == "Иван"
    assert data[0]["age"] == "25"
    assert data[0]["city"] == "Москва"
    assert data[1]["name"] == "Петр"
    assert data[1]["city"] == "СПб"


def test_csv_to_json_empty_file(tmp_path):
    """Тест с пустым CSV файлом"""
    csv_file = tmp_path / "test.csv"
    csv_file.write_text("", encoding="utf-8")

    json_file = tmp_path / "test.json"

    with pytest.raises(ValueError, match="CSV-файл пустой"):
        csv_to_json(str(csv_file), str(json_file))


def test_csv_to_json_only_header(tmp_path):
    """Тест с CSV файлом, содержащим только заголовок"""
    csv_file = tmp_path / "test.csv"
    csv_file.write_text("name,age,city", encoding="utf-8")

    json_file = tmp_path / "test.json"

    with pytest.raises(ValueError, match="CSV-файл не содержит данных"):
        csv_to_json(str(csv_file), str(json_file))


def test_csv_to_json_file_not_found():
    """Тест с несуществующим CSV файлом"""
    with pytest.raises(FileNotFoundError, match="CSV-файл не найден"):
        csv_to_json("nonexistent.csv", "output.json")


def test_csv_to_json_wrong_extension():
    """Тест с неправильным расширением файла"""
    with pytest.raises(ValueError, match="Входной файл должен иметь расширение .csv"):
        csv_to_json("file.txt", "output.json")


def test_json_csv_round_trip(tmp_path):
    """Тест на обратимость: JSON -> CSV -> JSON"""
    original_data = [
        {"id": "1", "name": "Тест", "active": "true"},
        {"id": "2", "name": "Пример", "active": "false"},
    ]

    json_file1 = tmp_path / "original.json"
    json_file1.write_text(
        json.dumps(original_data, ensure_ascii=False), encoding="utf-8"
    )

    csv_file = tmp_path / "converted.csv"
    json_to_csv(str(json_file1), str(csv_file))

    json_file2 = tmp_path / "back.json"
    csv_to_json(str(csv_file), str(json_file2))

    with open(json_file2, "r", encoding="utf-8") as f:
        round_trip_data = json.load(f)

    assert len(round_trip_data) == len(original_data)
    for i in range(len(original_data)):
        for key in original_data[i]:
            assert round_trip_data[i][key] == original_data[i][key]


def test_csv_to_json_empty_values(tmp_path):
    """Тест с пустыми значениями в CSV"""
    csv_file = tmp_path / "test.csv"
    csv_content = """name,age,city
Иван,25,
Петр,,СПб"""
    csv_file.write_text(csv_content, encoding="utf-8")

    json_file = tmp_path / "test.json"
    csv_to_json(str(csv_file), str(json_file))

    with open(json_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    assert data[0]["name"] == "Иван"
    assert data[0]["age"] == "25"
    assert data[0]["city"] == ""
    assert data[1]["name"] == "Петр"
    assert data[1]["age"] == ""
    assert data[1]["city"] == "СПб"

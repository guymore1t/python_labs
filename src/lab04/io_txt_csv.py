from pathlib import Path
from typing import Iterable, Sequence
import csv


def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    """чтобы выбрать кодировку, напишите ее название после encoding="""
    with open(path, "r", encoding=encoding) as file:
        return file.read()


def write_csv(
    rows: list[tuple | list], path: str | Path, header: tuple[str, ...] | None = None
) -> None:
    p = Path(path)
    if p.suffix.lower() != ".csv":
        raise ValueError("Должен быть csv файл")
    rows_list = list(rows)
    Path(path).parent.mkdir(parents=True, exist_ok=True)

    if rows:
        first_row_length = len(rows[0])
        for i, row in enumerate(rows):
            if len(row) != first_row_length:
                raise ValueError

    if header is not None and rows_list and len(header) != len(rows_list[0]):
        raise ValueError

    with p.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if header is not None:
            w.writerows(header)
        w.writerows(rows_list)

import argparse
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__),'..', 'lab05'))

from json_csv import json_to_csv, csv_to_json
from csv_xlsx import csv_to_xlsx

def main():
    parser = argparse.ArgumentParser(description="Конвертер данных", add_help=False)
    subparsers = parser.add_subparsers(dest="cmd", help="доступные команды")

    parser_json2csv = subparsers.add_parser("json2csv", help="Конвертировать JSON в CSV", add_help=False)
    parser_json2csv.add_argument("--in", dest="input", required=True, help="Входной JSON файл")
    parser_json2csv.add_argument("--out", dest="output", required=True, help="Выходной CSV файл")
    parser_json2csv.add_argument("-h", "--help", action="help", help="Показать эту справку и выйти")

    parser_csv2json = subparsers.add_parser("csv2json", help="Конвертировать CSV в JSON", add_help=False)
    parser_csv2json.add_argument("--in", dest="input", required=True, help="Входной CSV файл")
    parser_csv2json.add_argument("--out", dest="output", required=True, help="Выходной JSON файл")
    parser_csv2json.add_argument("-h", "--help", action="help", help="Показать эту справку и выйти")

    parser_csv2xlsx = subparsers.add_parser("csv2xlsx", help="Конвертировать CSV в XLSX", add_help=False)
    parser_csv2xlsx.add_argument("--in", dest="input", required=True, help="Входной CSV файл")
    parser_csv2xlsx.add_argument("--out", dest="output", required=True, help="Выходной XLSX файл")
    parser_csv2xlsx.add_argument("-h", "--help", action="help", help="Показать эту справку и выйти")

    parser.add_argument("-h", "--help", action="help", help="Показать справку и выйти")

    args = parser.parse_args()

    if not args.cmd:
        return
    
    try:
        if args.cmd == "json2csv":
            json_to_csv(args.input, args.output)
            print(f"Успешно сконвертирован {args.input} в {args.output}")

        elif args.cmd == "csv2json":
            csv_to_json(args.input, args.output)
            print(f"Успешно сконвертирован {args.input} в {args.output}")

        elif args.cmd == "csv2xlsx":
            csv_to_xlsx(args.input, args.output)
            print(f"Успешно сконвертирован {args.input} в {args.output}")

    except FileNotFoundError as e:
        print(f"Ошибка: Файл не найден - {e}")
        sys.exit(1)

    except ValueError as e:
        print(f"Ошибка: Неверные данные - {e}")
        sys.exit(1)

    except Exception as e:
        print(f"Неизвестная ошибка: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
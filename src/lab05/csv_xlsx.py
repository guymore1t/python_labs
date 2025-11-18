from openpyxl import Workbook
import csv
import os

def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    if not csv_path.lower().endswith('.csv'):
        raise ValueError('Неверный тип файла, ожидается csv')
    if not xlsx_path.lower().endswith('.xlsx'):
        raise ValueError('Неверный тип файла, ожидается xlsx')
    
    if not os.path.exists(csv_path):
        raise FileNotFoundError('Файл не найден')
    
    try:
        with open(csv_path, 'r', encoding='utf-8') as csv_file:
            csv_reader = csv.reader(csv_file)
            csv_data = list(csv_reader)
    except UnicodeDecodeError:
        raise ValueError('Ошибка кодировки, ожидается utf-8')
    
    if not csv_data:
        raise ValueError('csv файл пуст')
    
    wb = Workbook()
    ws = wb.active
    ws.title = 'Sheet1'

    for row in csv_data:
        ws.append(row)
    
    for column in ws.columns:
        max_length = 0
        column_letter = column[0].column_letter
        for cell in column:
            try:
                max_length = max(max_length, len(str(cell.value)))
            except:
                pass

            
        adjusted_width = max(max_length + 2, 8)

        ws.column_dimensions[column_letter].width = adjusted_width

    wb.save(xlsx_path)

if __name__ == "__main__":
    csv_to_xlsx("data/samples/cities.csv", "data/out/result3.xlsx")

import sys
from pathlib import Path
import os

current_dir = Path(__file__).parent
sys.path.insert(0, str(current_dir))

from src.lab09.group import Group
from src.lab08.models import Student

def test_group_class():
    print("Тестирование класса Group")
    print("=" * 30)
    
    # Используем ТЕСТОВЫЙ файл, а не основной
    test_file = "data/lab09/test_students.csv"
    
    # Удаляем тестовый файл перед началом теста (чтобы начать с чистого листа)
    if os.path.exists(test_file):
        os.remove(test_file)
    
    group = Group(test_file)
    
    print("1. Тест добавления")
    student = Student("Тест Студент", "2000-01-01", "ТЕСТ-00", 3.5)
    group.add(student)
    
    print("2. Тест чтения")
    students = group.list()
    print(f"Количество студентов: {len(students)}")
    for s in students:
        print(f"  - {s.fio}")
    
    print("3. Тест поиска")
    found = group.find("Тест")
    print(f"Найдено: {len(found)} студентов")
    
    print("4. Тест обновления")
    success = group.update("Тест Студент", gpa=4.0)
    print(f"Обновление: {'успешно' if success else 'не удалось'}")
    
    print("5. Тест удаления")
    success = group.remove("Тест Студент")
    print(f"Удаление: {'успешно' if success else 'не удалось'}")
    
    print("\nТестирование завершено")
    
    # Показываем содержимое файла
    print("\nСодержимое файла после теста:")
    if os.path.exists(test_file):
        with open(test_file, 'r') as f:
            print(f.read())
    else:
        print("Файл не существует")

if __name__ == "__main__":
    test_group_class()
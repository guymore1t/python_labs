import sys
from pathlib import Path

current_dir = Path(__file__).parent
sys.path.insert(0, str(current_dir))

from src.lab09.group import Group
from src.lab08.models import Student

def demo_crud_operations():
    print("Демонстрация CRUD операций")
    print("=" * 40)
    
    group = Group("data/lab09/students.csv")
    
    print("1. Добавляем студентов")
    student1 = Student("Иванов Иван", "2003-10-10", "БИВТ-21-1", 4.3)
    student2 = Student("Петрова Анна", "2002-05-15", "БИВТ-21-2", 4.7)
    student3 = Student("Сидоров Алексей", "2004-03-22", "БИВТ-20-3", 3.9)
    
    group.add(student1)
    group.add(student2)
    group.add(student3)
    
    print("2. Все студенты:")
    for i, student in enumerate(group.list(), 1):
        print(f"{i}. {student.fio}, {student.group}, GPA: {student.gpa}")
    
    print("\n3. Поиск по 'Иванов':")
    found = group.find("Иванов")
    for student in found:
        print(f"Найден: {student.fio}")
    
    print("\n4. Обновляем данные Иванова:")
    group.update("Иванов Иван", gpa=4.5, group="БИВТ-22-1")
    
    print("\n5. Удаляем Петрову:")
    group.remove("Петрова Анна")
    
    print("\n6. Финальный список:")
    for i, student in enumerate(group.list(), 1):
        print(f"{i}. {student.fio}, {student.group}, GPA: {student.gpa}")

if __name__ == "__main__":
    demo_crud_operations()
import json
from pathlib import Path
from typing import List
from .models import Student

def students_to_json(students: List[Student], path: str) -> None:
    data = [student.to_dict() for student in students]
    file_path = Path(path)
    file_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def students_from_json(path: str) -> List[Student]:
    file_path = Path(path)
    
    if not file_path.exists():
        raise FileNotFoundError(f"Файл не найден: {path}")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    if not isinstance(data, list):
        raise ValueError("Ожидается список студентов в JSON файле")
    
    students = []
    
    for i, item in enumerate(data):
        required_fields = ['fio', 'birthdate', 'group', 'gpa']
        for field in required_fields:
            if field not in item:
                raise ValueError(f"Отсутствует обязательное поле '{field}' у студента {i}")
        
        student = Student.from_dict(item)
        students.append(student)
    
    return students
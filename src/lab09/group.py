import csv
from pathlib import Path
import sys

current_dir = Path(__file__).parent
project_root = current_dir.parent.parent
sys.path.insert(0, str(project_root))

from src.lab08.models import Student

class Group:
    def __init__(self, storage_path: str):
        self.path = Path(storage_path)
        self._ensure_storage_exists()
    
    def _ensure_storage_exists(self):
        if not self.path.exists():
            self.path.parent.mkdir(parents=True, exist_ok=True)
            with open(self.path, 'w', encoding='utf-8', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['fio', 'birthdate', 'group', 'gpa'])
    
    def _read_all(self):
        students = []
        
        if not self.path.exists():
            return students
        
        with open(self.path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                student = Student(
                    fio=row['fio'],
                    birthdate=row['birthdate'],
                    group=row['group'],
                    gpa=float(row['gpa'])
                )
                students.append(student)
        
        return students
    
    def list(self):
        return self._read_all()
    
    def add(self, student: Student):
        with open(self.path, 'a', encoding='utf-8', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([student.fio, student.birthdate, 
                           student.group, student.gpa])
    
    def find(self, substr: str):
        all_students = self._read_all()
        found_students = []
        
        for student in all_students:
            if substr.lower() in student.fio.lower():
                found_students.append(student)
        
        return found_students
    
    def remove(self, fio: str):
        students = self._read_all()
        new_students = []
        removed = False
        
        for student in students:
            if student.fio != fio:
                new_students.append(student)
            else:
                removed = True
        
        if removed:
            with open(self.path, 'w', encoding='utf-8', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['fio', 'birthdate', 'group', 'gpa'])
                
                for student in new_students:
                    writer.writerow([student.fio, student.birthdate, 
                                   student.group, student.gpa])
            return True
        else:
            return False
    
    def update(self, fio: str, **fields):
        students = self._read_all()
        updated = False
        
        for student in students:
            if student.fio == fio:
                for field_name, new_value in fields.items():
                    if hasattr(student, field_name):
                        setattr(student, field_name, new_value)
                        updated = True
        
        if updated:
            with open(self.path, 'w', encoding='utf-8', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['fio', 'birthdate', 'group', 'gpa'])
                
                for student in students:
                    writer.writerow([student.fio, student.birthdate, 
                                   student.group, student.gpa])
            return True
        else:
            return False
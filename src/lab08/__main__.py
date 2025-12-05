import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from src.lab08.models import Student
from src.lab08.serialize import students_to_json, students_from_json

def main():
    project_root = Path(__file__).parent.parent.parent
    input_path = project_root / "data" / "lab08" / "students_input.json"
    output_path = project_root / "data" / "lab08" / "students_output.json"
    
    input_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    loaded_students = students_from_json(str(input_path))
    
    for student in loaded_students:
        print(f"{student.fio} ({student.group}), {student.age()} лет, GPA {student.gpa:.2f}")
    
    students_to_json(loaded_students, str(output_path))

if __name__ == "__main__":
    main()
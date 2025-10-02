def format_record(rec: tuple[str, str, float]) -> str:

    fio, group, gpa = rec

    if not isinstance(fio, str) or not fio.strip():
        raise ValueError
    
    if not isinstance(group, str) or not group.strip():
        raise ValueError
    
    if not isinstance(gpa, (int, float)):
        raise TypeError

    cleanned_fio = ' '.join(fio.split())

    fio_parts = cleanned_fio.split()

    if len(fio_parts) < 2:
        raise ValueError    
    
    surname = fio_parts[0].title()

    initials = []

    for name_part in fio_parts[1:]:
        if name_part.strip():
            initial = name_part[0].upper() + '.'
            initials.append(initial)

    if len(initials) > 2:
        initials = initials[:2]

    formatted_fio = f"{surname} {''.join(initials)}"

    cleaned_group = group.strip()

    formatted_gpa = f"{gpa:.2f}"

    return f"{formatted_fio}, гр. {cleaned_group}, GPA {formatted_gpa}"

student1 = ("Иванов Иван Иванович", "BIVT-25", 4.6)
student2 = ("Петров Пётр", "IKBO-12", 5.0)
student3 = ("Петров Пётр Петрович", "IKBO-12", 5.0)
student4 = ("  сидорова  анна   сергеевна ", "ABB-01", 3.999)

print(format_record(student1))
print(format_record(student2))
print(format_record(student3))
print(format_record(student4))
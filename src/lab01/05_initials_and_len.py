name = input('ФИО: ')

name2 = name.strip()
length = len(name2)

parts = name2.split()
initials = ''.join(word[0].upper() for word in parts)

print('Инициалы:', initials)
print('Длина(символов):',length)


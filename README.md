# python_labs

## Лабораторная работа 1

# Задание 1

```
name = input()
age = int(input())

print('Привет,' ,name ,'! Через год тебе будет', age +1)
```
![Картинка 1](./images/lab01/01.png)

# Задание 2

```
a = float(input())
b = float(input())
print('a:' ,a)
print('b:', b)
print('sum=',a + b,'avg=',((a + b) / 2))
```

![Картинка2](./images/lab01/02.png)

# Задание 3

```
price = float(input())
discount = float(input())
vat = float(input())

base = price * (1 - discount/100)
vat_amount = base * (vat/100)
total = base + vat_amount

print('База после скидки: ',base,'0 ₽',sep = '')
print('НДС: ',vat_amount,'0 ₽',sep = '')
print('Итого к оплате: ',total,'0 ₽',sep = '')
```

![Картинка3](./images/lab01/03.png)

# Задание 4
```
min1 = int(input())

hours = min1 // 60
min2 = min1 % 60

if min1 % 60 != 0:
    print(hours,':',min2,sep = '')

else:
    print(hours,':',min2,'0',sep = '')
    
```

![Картинка4](./images/lab01/04.png)

# Задание 5
```
name = input('ФИО: ')

name2 = name.strip()
length = len(name2)

parts = name2.split()
initials = ''.join(word[0].upper() for word in parts)

print('Инициалы:', initials)
print('Длина(символов):',length)
    
```

![Картинка5](./images/lab01/05.png)

# Задание 6
```
n = int(input())
och = 0
zaoch = 0

for a in range(n):
    line = input().split()
    form = line[-1]
    if form == 'True':
        och +=1 
    else:
        zaoch +=1

print(och, zaoch)
```

![Картинка6](./images/lab01/06.png)

## Лабораторная работа 2

# Задание 1


# min_max

```py
def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:

    if len(nums) == 0:
        raise ValueError
    
    return(min(nums), max(nums))
```

![Картинка7](./images/lab02/arrays01.png)

# unique_sorted

```py
def unique_sorted(nums: list[float | int]) -> list[float | int]:

    if len(nums) == 0:
        return []

    return(sorted(set(nums)))
```

![Картинка8](./images/lab02/arrays02.png)

# flatten

```py
def flatten(mat: list[list | tuple]) -> list:

    res = []

    for element in mat:
        if isinstance(element, list) or isinstance(element, tuple):
            for inner_element in element:
                res.append(inner_element)
        else:
            raise TypeError
        
    return res
```

![Картинка9](./images/lab02/arrays03.png)

# Задание 2

# transpose

```py
def transpose(mat: list[list[float or int]]) -> list[list]:
    if len(mat) == 0:
        return []
    
    for row in mat:
        if len(mat[0]) != len(row):
            raise ValueError
        
    res = []

    row_cnt = len(mat)
    stolb_cnt = len(mat[0])

    for stolb_index in range(stolb_cnt):
        new_row = []
        for row_index in range(row_cnt):
            new_row.append(mat[row_index][stolb_index])
        res.append(new_row)

    return res

```
![Картинка10](./images/lab02/matrix01.png)

# row_sums

```py
def row_sums(mat: list[list[float or int]]) -> list[float]:

    for row in mat:
        if len(mat[0]) != len(row):
            raise ValueError
        
    res = [sum(row) for row in mat]

    return res
```
![Картинка11](./images/lab02/matrix02.png)

# col_sums

```py
def col_sums(mat: list[list[float | int]]) -> list[float]:

    for row in mat:
        if len(mat[0]) != len(row):
            raise ValueError

    res = [sum(row) for row in zip(*mat)]

    return res

```
![Картинка12](./images/lab02/matrix03.png)

# Задание 3

```py
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

```
![Картинка13](./images/lab02/tuples01.png)

## Лабораторная работа 3

# Задание А

# normalize

```py
def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:

    text = text.replace('Ё','E')
    text = text.replace('ё','е')
    text = text.replace('\r',' ').replace('\t',' ').replace('\n',' ')
    text = text.split()
    text2 = ' '.join(text)
    text3 = text2.casefold()
    return text3

t1 = "ПрИвЕт\nМИр\t"
t2 = "ёжик, Ёлка"
t3 = "Hello\r\nWorld"
t4 = "  двойные   пробелы  "

print(normalize(t1), normalize(t2), normalize(t3), normalize(t4), sep='\n')
```

![картинка14](./images/lab03/normalize.png)

# tokenize

```py
import re 

def tokenize(text: str) -> list[str]:
    pattern = r'\w+(?:-\w+)*'
    return re.findall(pattern, text)

t1 = "привет мир"
t2 = "hello,world!!!"
t3 = "по-настоящему круто"
t4 = "2025 год"
t5 = "emoji 😀 не слово"

print(tokenize(t1), tokenize(t2),tokenize(t3),tokenize(t4),tokenize(t5),sep='\n')
```

![картинка15](./images/lab03/tokenize.png)

# count_freq + top_n

```py
def count_freq(tokens: list[str]) -> dict[str, int]:
    freq = {}  
    
    for token in tokens:  
        if token in freq:  
            freq[token] += 1  
        else: 
            freq[token] = 1 

    items = list(freq.items())
    items.sort(key = lambda item: (-item[1], item[0]))
    
    return items

tokens1 = ["a","b","a","c","b","a"]
tokens2 = ["bb","aa","bb","aa","cc"]
print(count_freq(tokens1))
print(count_freq(tokens2))
```

![картинка16](./images/lab03/count_freq.png)

## Задание B

```py
import sys
from lib import text

input_text = sys.stdin.readline()

normalized_text = text.normalize(input_text, casefold = True, yo2e = True)
tokens = text.tokenize(normalized_text)
freq = text.count_freq(tokens)

words_count = len(tokens)
unique_words = len(freq)
top_5 = freq[:5]    

print(f"Всего слов: {words_count}")
print(f"Уникальных слов: {unique_words}")
print("Топ-5:")

for word, count in top_5:
    print(f'{word}:{count}')
```

![картинка17](./images/lab03/test_stats.png)

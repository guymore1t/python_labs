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

```
def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:

    if len(nums) == 0:
        raise ValueError
    
    return(min(nums), max(nums))

def unique_sorted(nums: list[float | int]) -> list[float | int]:

    if len(nums) == 0:
        return []

    return(sorted(set(nums)))

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
# min_max

![Картинка7](./images/lab02/arrays01.png)

# unique_sorted

![Картинка8](./images/lab02/arrays02.png)

# flatten

![Картинка9](./images/lab02/arrays03.png)

# Задание 2

# transpose

```
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

```
def row_sums(mat: list[list[float or int]]) -> list[float]:

    for row in mat:
        if len(mat[0]) != len(row):
            raise ValueError
        
    res = [sum(row) for row in mat]

    return res
```
![Картинка11](./images/lab02/matrix02.png)

# col_sums

```
def col_sums(mat: list[list[float | int]]) -> list[float]:

    for row in mat:
        if len(mat[0]) != len(row):
            raise ValueError

    res = [sum(row) for row in zip(*mat)]

    return res

```
![Картинка12](./images/lab02/matrix03.png)






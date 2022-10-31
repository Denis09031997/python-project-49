# Получаем рандомное число любое
import random
from re import I


random_num = random.randint(2, 30)
print(f'Получили рандомное число: {random_num}')

# узнать на какие числа делится без остатка
dividers = []

i = 1

while i <= random_num:
    if random_num % i == 0:
        dividers.append(i)
    i = i + 1


print(f'Список делителй числа {random_num} : {dividers}')

if len(dividers) == 2:
    result = 'yes'
    print(result)
else:
    result = 'no'
    print(result)
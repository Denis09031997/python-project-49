import random



# Формируем ряд случайных чисел
row_length = random.randint(5, 10)
print(f'Длина ряда будет - {row_length}')
series_num = []
start_num = random.randint(1, 100)
print(f'Стартовое число будет: {start_num}')
series_num.append(start_num)
print(f'Ряд чисел будет начинаться с: {series_num}')
interval = random.randint(1, 5)
print(f'Интервал будет - {interval}')

i = 0

while len(series_num) < row_length:
    series_num.append(series_num[-1] + interval)

print(f'Итоговый список случайных чисел: {series_num}')
#print((' '.join(map(str, series_num))))


# пропускаем случайное число в ряду
print('-----------------------------')
index_missing = random.randint(0, len(series_num))
print('Индекс пропущенного числа - ' + str(index_missing))
print(f'Пропущенное число из списка: {series_num} это - {series_num[index_missing]}')
row_missing_num = series_num
print(f'Предитог: {row_missing_num}')
row_missing_num[index_missing] = '..'
line_row = ' '.join(map(str, series_num))
print('Строчка чисел с пропуском - ' + line_row)

    

#print(series_num)
#print(' '.join(map(str, series_num)))

#-------------------
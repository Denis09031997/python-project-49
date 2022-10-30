import random
import prompt


print('Welcome to the Brain Games!')


def play_progression():
    i = 0
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!\nWhat number is missing in the progression?.')
    while i < 3:
        row_length = random.randint(5, 10)
        series_num = []
        start_num = random.randint(1, 100)
        series_num.append(start_num)
        interval = random.randint(1, 5)
        while len(series_num) < row_length:
            series_num.append(series_num[-1] + interval)
        index_missing = random.randint(0, len(series_num))
        search_num = series_num[index_missing]
        row_missing_num = series_num
        row_missing_num[index_missing] = '..'
        line_row = ' '.join(map(str, series_num))
        print(f'Question: {line_row}')
        answer = prompt.string('Your answer: ')
        if answer == str(search_num):
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{search_num}'\nLet's try again, {name}")
            break
        i = i + 1

print(play_progression())
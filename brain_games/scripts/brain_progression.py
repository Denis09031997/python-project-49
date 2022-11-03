import random
import prompt


def main():
    print('Welcome to the Brain Games!')
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
        index_missing = random.randint(0, len(series_num) - 1)
        search_num = series_num[index_missing]
        row_missing_num = series_num
        row_missing_num[index_missing] = '..'
        line_row = ' '.join(map(str, series_num))
        print(f'Question: {line_row}')
        answer = prompt.string('Your answer: ')
        if answer == str(search_num):
            print('Correct!')
        else:
            print(
                f"'{answer}' is wrong answer ;(. Correct "
                f"answer was '{search_num}'\nLet's try again, {name}!"
            )
            break
        i = i + 1
    if i == 3:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()

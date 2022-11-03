import random
import prompt


def main():
    print('Welcome to the Brain Games!')
    i = 0
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!\nAnswer "yes" if the number is even, '
    'otherwise answer "no".')
    while i < 3:
        num = random.randint(1, 100)
        print(f'Question: {num}')
        answer = prompt.string('Your answer: ')
        if answer != 'yes' and answer != 'no':
            print(f'{answer} is wrong answer ;(. Let\'s try again, {name}!')
            break
        elif num % 2 == 0 and answer == 'yes':
            print('Correct!')
        elif num % 2 != 0 and answer == 'no':
            print('Correct!')
        elif num % 2 != 0 and answer == 'yes':
            print(f"'yes' is wrong answer ;(. Correct answer "
            "was 'no'.\nLet's try again, {name}!")
            break
        elif num % 2 == 0 and answer == 'no':
            print(f"'no' is wrong answer ;(. Correct answer "
            "was 'yes'.\nLet's try again, {name}!")
            break
        i = i + 1
    if i == 3:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()

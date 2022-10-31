import prompt
import random


print('Welcome to the Brain Games!')


def play_prime():
    i = 0
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!\nAnswer "yes" if given number is prime. Otherwise answer "no".')
    while i < 3:
        random_num = random.randint(2, 30)
        dividers = []
        index = 1
        while index <= random_num:
            if random_num % index == 0:
                dividers.append(i)
            index = index + 1
        if len(dividers) == 2:
            result = 'yes'
        else:
            result = 'no'
        print(f'Question: {random_num}')
        answer = prompt.string('Your answer: ')
        if answer == 'yes' and len(dividers) == 2:
            print('Correct!')
        elif answer == 'no' and len(dividers) != 2:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{result}'\nLet's try again, {name}")
            break
        i = i + 1


print(play_prime())

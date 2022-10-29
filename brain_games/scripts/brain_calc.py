import random
import prompt


print('Welcome to the Brain Games!')


def play_brain_calc():
    i = 0
    operations = ['+', '-', '*']
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!\nWhat is the result of the expression?')
    while i < 3:
        op = random.choice(operations)
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        print(f'Question: {num1} {op} {num2}')
        answer = prompt.string('Your answer: ')
        if op == '+':
            result = num1 + num2
        elif op == '-':
            result = num1 - num2
        elif op == '*':
            result = num1 * num2
        if int(answer) == int(result):
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{result}'\nLet's try again, {name}")
            break
        i = i + 1


print(play_brain_calc())
import random
import prompt


def main():
    print('Welcome to the Brain Games!')
    index = 0
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!\nFind the greatest common divisor of given numbers.')
    while index < 3:
        num1 = random.randint(1, 1000)
        num2 = random.randint(1, 1000)
        list_num = [num1, num2]
        list_num.sort(reverse=True)
        remains = []
        remains.append(list_num[0] % list_num[1])
        remains.append(list_num[1] % remains[0])
        i = 0
        j = 1
        while (remains[i] % remains[j]) != 0:
            remains.append(remains[i] % remains[j])
            i = i + 1
            j = j + 1

        print(f'Question: {num1} {num2}')
        answer = prompt.string('Your answer: ')
        if int(answer) == remains[-1]:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{remains[-1]}'\nLet's try again, {name}")
            break
        index = index + 1


if __name__ == '__main__':
    main()

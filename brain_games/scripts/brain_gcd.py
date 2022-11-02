import random
import prompt


def main():
    print('Welcome to the Brain Games!')
    index = 0
    result = 0
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!\nFind the greatest common divisor of given numbers.')
    while index < 3:
        num1 = random.randint(1, 1000)
        num2 = random.randint(1, 1000)
        list_num = [num1, num2]
        list_num.sort(reverse=True)
        print(f'Question: {num1} {num2}')
        answer = prompt.string('Your answer: ')
        if list_num[0] % list_num[1] == 0 and list_num[1] % list_num[1] == 0:
            result = list_num[1]
        else:
            remains = []
            remains.append(list_num[0] % list_num[1])
            remains.append(list_num[1] % remains[0])
            i = 0
            j = 1
            while (remains[i] % remains[j]) != 0:
                if remains[j] == 0:
                    result = remains[i]
                    break
                remains.append(remains[i] % remains[j])
                result = remains[-1]
                i = i + 1
                j = j + 1
        if int(answer) == result:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{result}'\nLet's try again, {name}!")
            break
        index = index + 1
    if index == 3:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()

# Нахождение делителей

x = 140
y = 96

def find_remnants(num1, num2):
    remains = []
    if num1 > num2:
        first_remains = num1 % num2
        remains.append(first_remains)
        second_remains = num2 % first_remains
        remains.append(second_remains)
        return remains
    else:
        first_remains = num2 % num1
        remains.append(first_remains)
        second_remains = num1 % first_remains
        remains.append(second_remains)
        return remains
        

list_remains = find_remnants(x, y)

print(list_remains)


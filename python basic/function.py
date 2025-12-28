def sum():
    a, b = 5, 20
    print(a + b)

sum()

def clc(a, b=55):
    sum = a + b
    return sum

print(f'the age will be {clc(2) + 1} in a year')


calc = lambda num1, num2 : num1 + num2
print(calc(5, 2))
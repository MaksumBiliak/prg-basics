###
# Calculates the sum of the digits in a number

def sum_digits(number):
    str1=str(abs(number))
    sum=0
    for a in str1 :
        sum=int(a) + sum
    return sum

any_number = int(input('Enter integer number: '))
result = sum_digits(any_number)
print(f'The sum of the digits in the number {any_number} is {result}')
def is_armstrong(number):
    num_str = str(number)
    n = len(num_str)
    armstrong_sum = sum(int(digit) ** n for digit in num_str)
    return armstrong_sum == number

number = int(input("Enter a number: "))
if is_armstrong(number):
    print(number, "is an Armstrong number")
else:
    print(number, "is not an Armstrong number")

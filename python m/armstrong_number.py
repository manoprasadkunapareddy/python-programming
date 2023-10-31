def is_armstrong_number(number):
    num_str = str(number)
    num_digits = len(num_str)
    total = sum(int(digit)**num_digits for digit in num_str)
    return total == number

given_number = int(input("Enter number: "))

if is_armstrong_number(given_number):
    print("Given number is Armstrong number")
else:
    print("Given number is not Armstrong number")

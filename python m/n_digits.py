def find_single_digit_sum(n, number):
    while len(str(number)) > 1:
        total = sum(int(digit) for digit in str(number))
        number = total
    return number

N = int(input("Enter N value: "))
number = int(input(f"Enter {N} digit number: "))

if N == len(str(number)):
    single_digit_sum = find_single_digit_sum(N, number)
    print(f"Sum of {N} digit number: {single_digit_sum}")
else:
    print(f"The entered number is not {N} digits long.")

def find_single_digit_sum(n, num):
    while num >= 10:
        total = 0
        while num > 0:
            total += num % 10
            num //= 10
        num = total
    return num

N = int(input("Enter N value: "))
number = int(input(f"Enter {N} digit number: "))

if len(str(number)) != N:
    print(f"Error: Input should be a {N} digit number.")
else:
    result = find_single_digit_sum(N, number)
    print(f"Sum of {N} digit number: {result}")

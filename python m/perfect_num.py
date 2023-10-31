def is_perfect_number(num):
    divisors = [i for i in range(1, num) if num % i == 0]
    return sum(divisors) == num

given_number = int(input("Enter a number: "))

if is_perfect_number(given_number):
    print(f"{given_number} is a Perfect Number")
else:
    print(f"{given_number} is not a Perfect Number")

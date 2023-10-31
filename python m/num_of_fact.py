def find_factors(n):
    factors = []
    for i in range(1, n+1):
        if n % i == 0:
            factors.append(i)
    return factors

given_number = int(input("Enter a number: "))
n = int(input("Enter the value of N: "))

factors = find_factors(given_number)

print(f"Number of factors = {len(factors)}")

if len(factors) >= n:
    print(f"{n}th factor of {given_number} = {factors[n-1]}")
else:
    print(f"There is no {n}th factor of {given_number}")

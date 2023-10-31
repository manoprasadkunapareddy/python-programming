def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
N = int(input("enter the number"))
sum_factorials = sum(factorial(i) for i in range(1, N+1))
print(f"The sum of factorials from 1 to {N} is: {sum_factorials}")

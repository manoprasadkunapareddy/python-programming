def sum_of_squares(n):
    if n < 1:
        return "Please enter a positive integer greater than 0."
    
    sum_squares = (n * (n + 1) * (2 * n + 1)) // 6
    return sum_squares

n = int(input("Enter the value of N: "))

result = sum_of_squares(n)
print(f"The sum of the squares of the first {n} natural numbers is: {result}")

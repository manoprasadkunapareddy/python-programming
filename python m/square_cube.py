def calculate_square_and_cube(number):
    square = number ** 2
    cube = number ** 3
    return square, cube

given_number = float(input("Enter a decimal number: "))

square_number, cube_number = calculate_square_and_cube(given_number)

print(f"Square Number: {square_number}")
print(f"Cube Number: {cube_number}")

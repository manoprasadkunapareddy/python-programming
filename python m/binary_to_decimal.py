def binary_to_decimal(binary):
    decimal = int(binary, 2)
    return decimal

def decimal_to_octal(decimal):
    octal = oct(decimal).replace("0o", "")
    return octal

given_binary = input("Enter a binary number: ")

decimal_number = binary_to_decimal(given_binary)
octal_number = decimal_to_octal(decimal_number)

print(f"Decimal Number: {decimal_number}")
print(f"Octal: {octal_number}")

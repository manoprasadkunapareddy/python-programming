def create_tuple_list(lower, upper):
    tuple_list = [(x, x**2) for x in range(lower, upper+1)]
    return tuple_list

try:
    lower_range = int(input("Enter the lower range: "))
    upper_range = int(input("Enter the upper range: "))

    if lower_range <= upper_range:
        result = create_tuple_list(lower_range, upper_range)
        print(result)
    else:
        print("Error: Lower range should be less than or equal to upper range.")
except ValueError:
    print("Error: Please enter valid integers for lower and upper range.")

def count_vowels_and_consonants(statement):
    vowels = "aeiouAEIOU"
    num_vowels = 0
    num_consonants = 0

    for char in statement:
        if char.isalpha():
            if char in vowels:
                num_vowels += 1
            else:
                num_consonants += 1

    return num_vowels, num_consonants

given_statement = "Saveetha School of Engineering Sample"

num_vowels, num_consonants = count_vowels_and_consonants(given_statement)

print(f"Number of vowels = {num_vowels} Number of Consonants = {num_consonants}")

if num_vowels > num_consonants:
    print("Vowels are maximum.")
elif num_vowels < num_consonants:
    print("Consonants are maximum.")
else:
    print("Both vowels and consonants are equal.")

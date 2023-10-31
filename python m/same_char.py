def count_matching_characters(s1, s2):
    matches = 0
    
    for i in range(len(s1)):
        if s1[i] == s2[i]:
            matches += 1
    
    return matches


s1 = input("Enter the first string: ")
s2 = input("Enter the second string: ")


result = count_matching_characters(s1, s2)

if type(result) == int:
    print(f"The number of matching characters is: {result}")
else:
    print(result)

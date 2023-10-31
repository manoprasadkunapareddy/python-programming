def count_lines_and_words(para):
    lines = para.split('\n')
    num_lines = len(lines)
    
    print(f"Number of lines: {num_lines}")
    print("Number of words in each line:")
    
    for i, line in enumerate(lines, start=1):
        words = line.split()
        num_words = len(words)
        print(f"Line {i} {num_words}")

paragraph = '''
This is the most straightforward way to count the number
of lines in a text file in Python. The readlines() method reads all
lines from a file and stores it in a list. Next, use the len() function
to find the length of the list which is nothing but total lines present in a file.
'''

count_lines_and_words(paragraph)

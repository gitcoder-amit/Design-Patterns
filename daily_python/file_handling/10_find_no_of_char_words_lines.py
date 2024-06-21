f = open('data.txt', mode='r')
no_of_words = 0
no_of_chars = 0
no_of_lines = 0

for line in f:
    no_of_lines += 1
    line = line.strip("\n")  # now not contains \n  
    no_of_chars += len(line)
    list1 = line.split()
    no_of_words += len(list1)

print(f"no_of_chars {no_of_chars}", f"no_of_words, {no_of_words}", f"no_of_lines {no_of_lines}")

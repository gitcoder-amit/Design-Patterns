# print("enter age")

f = open("data.txt", 'r')
print(f.read())
f.close()


age = input('enter your age')
f = open("data.txt", 'w')
f.write(age)


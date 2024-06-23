import os
path = input("Enter the path:")  # /home/amityadav/Pictures
path = path.replace('\\', '/')  # due to one is a excape sequence  we don't need to change due to ubuntu stores forward slash already
print(path)  # /home/amityadav/Pictures 
# rename(old_name, new_name)
print(os.listdir(path))  # [] list of all the files

def main():
    i = 1
    for filename in os.listdir(path):
        new_name = path+f'screenshot {i}.jpg'
        old_name = path+filename
        os.rename(old_name, new_name)
        i += 1 

main()
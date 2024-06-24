'''
In this video 1. Python program to fetch header of CSV file
              2. Python program to check CSV file data format is valid or not
'''


import csv


def check_csv(file):
    with open('titanic.csv', 'r') as f:
        my_data = csv.reader(f, delimiter = ',')
        print(my_data)  #iterator
        header = next(my_data)
        # print(len(header)) # no of columns
        no_of_columns = len(header)
        for rec in my_data:
            if len(rec) != no_of_columns:
                return False
        return True

detector = check_csv('titanic.csv')
if detector:
    print("valid data")
else:
    print("invalid data")
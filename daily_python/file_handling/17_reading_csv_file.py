'''
    How to read CSV file?
       i) In the form of list
       ii) In the form of dictionary

    2. Python Program to check CSV file data format is valid or not
'''

import csv

with open('titanic.csv', 'r') as f:
    # csv.register_dialect('normal_dialect', delimiter=',', quotechar='"')  # when we want to say inside double quote for one single column
    # titanic_data = csv.reader(f, delimiter = ',')
    # print(titanic_data)

    # for rec in titanic_data:
    #     print(rec)                # data in list

    titanic_data = csv.DictReader(f, delimiter=',')  # DictReader
    for rec in titanic_data:
        if rec['Age'] != '':
            if int(rec['Age']) >30  and rec['Age'] != '':
                print(rec) 
        print(rec['Age'])       
# {'PassengerId': '385', 'Survived': '0', 'Pclass': '3', 'Name': 'Plotcharsky, Mr. Vasil', 'Sex': 'male', 'Age': '', 'SibSp': '0', 'Parch': '0', 'Ticket': '349227', 'Fare': '7.8958', 'Cabin': '', 'Embarked': 'S'}
# {'PassengerId': '386', 'Survived': '0', 'Pclass': '2', 'Name': 'Davies, Mr. Charles Henry', 'Sex': 'male', 'Age': '18', 'SibSp': '0', 'Parch': '0', 'Ticket': 'S.O.C. 14879', 'Fare': '73.5', 'Cabin': '', 'Embarked': 'S'}

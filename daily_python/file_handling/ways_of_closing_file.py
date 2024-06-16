'''
Ways of Closing file ->
    1. Normal  Way
    2. Using exception Handling
    3. with statement

    Normal Way --> f = open("file_name")
                # operation --> if exception occur there is not guaranty file will be closed so it is not a a safer method
                 f.close()

    Using exception handling ->
                try:
                    f = open('filename', mod='r')
                    # operations
                finally:
                    f.close()   # always executes hence file will be closed everytime

    with statement -> 
                with open('filename', mode='r') as f:   # here automatically file we closed no need to worry about closing file
                    #operations
'''

with open('data.txt', mode='r') as f:  # best way
    print(f.read())

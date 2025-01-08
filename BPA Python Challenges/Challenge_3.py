import math 
numbers=[1, 2, 3, 4, 5, 6, 7, 8 , 9, 10, 11, 12] 

def even(inputnumbers):
    for item in inputnumbers: # for items(each number) in the list it will remove numbers that are not even
        if item % 2 == 0: # if item is even it pass's
            pass
        else: # else (so not even) are removed
            inputnumbers.remove(item)
    return inputnumbers # returns numbers with odd numbers removed

print(even(numbers)) # prints

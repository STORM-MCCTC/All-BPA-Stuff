import math
numbers=[1, 2, 3, 4, 5, 6, 7, 8 , 9, 10, 11, 12]

def even(inputnumbers):
    for item in inputnumbers:
        if item % 2 == 0:
            pass
        else:
            inputnumbers.remove(item)
    return inputnumbers

print(even(numbers))

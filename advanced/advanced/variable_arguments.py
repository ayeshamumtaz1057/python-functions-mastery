"""
*args Example
"""

def total(*numbers):

    sum = 0

    for num in numbers:
        sum += num

    return sum


print(total(10,20,30))

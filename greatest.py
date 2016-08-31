# Define a procedure, greatest,
# that takes as input a list
# of positive numbers, and
# returns the greatest number
# in that list. If the input
# list is empty, the output
# should be 0.

def greatest(list_of_numbers):
    b = 0
    for a in list_of_numbers:
        if b <= a:
            b = a
    return b

print greatest([4,23,1])
# >>> 23
print greatest([])
# >>> 0



# Write a python function that will take n as input and print the pattern of n rows. If the n is even, then print it flipped.
# Example:

# n=3
# *
# * *
# * * *

# n=4
# * * * *
# * * *
# * *
# *

def even_odd(num):
  '''This checks if a number is even or odd'''
    if num % 2 == 0:
        result="Even"

    else:
        result="Odd"
    return result


def patterns(n):
  '''depending the odd/even of number this function prints "*"s '''

    if even_odd(n) == "Odd":
        for i in range(1,n+1):
            for j in range(1,i+1):
                print("*", end=' ')
            print()
    else:
        for i in range(n, 0, -1):
            for j in range(1,i+1):
                print("*", end=' ')
            print()
patterns(5)

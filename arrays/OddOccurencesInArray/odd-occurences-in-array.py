# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here
    # initialize variable for the result
    result = 0
    # The problem is basically asking for the unique number in a series of numbers
    # unique numbers in place of duplicates have special properties and using xor
    # retrieving the unique number is easy
    for number in A:
        # xor all numbers to find the unique number
        result ^= number
    return result

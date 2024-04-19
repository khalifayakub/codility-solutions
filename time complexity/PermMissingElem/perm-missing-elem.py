# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here O(N) time complexity
    # edge case: if array is empty, the answer is always 1
    if len(A) == 0:
        return 1
    # save sum of elements in A
    sum = 0
    # n will keep track of the maximum number in the array
    n = 0
    for number in A:
        sum += number
        n = max(n, number)
    # formula below gives the sum of the permutation of number from 1..n
    total = (n * (n+1))//2
    # edge case: if the total and sum is equal, means no missing element
    # that means you will just return the max + 1
    if total == sum:
        return n+1
    # subtracting the total from sum of elements will always give you the missing number in
    # the permutation
    return abs(total-sum)

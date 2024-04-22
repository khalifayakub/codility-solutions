def solution(A):
    # track sum of array cause we will use number theory
    sum_of_array = 0
    ## any repetition of a number means it is not a valid permutation
    if len(A) != len(list(set(A))):
        return 0
    # get length of array for number theory formula
    n = len(A)
    # get sum of array
    for number in A:
        sum_of_array += number
    # this formula gives you the sum of elements from 1..n
    total = (n * (n + 1)) // 2
    # if the total is the same as sum of array, that means no element is missing
    # if no element is missing, that means it is a valid permutation
    # else is not a valid permutation
    return 1 if total == sum_of_array else 0

print(solution([1,4,1]))
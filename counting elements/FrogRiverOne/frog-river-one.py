# get the first time each element comes and then get the max

def solution(x, A):
    # count element array since we know max is x
    arr = [-1] * x
    n = len(A)
    for i in range(n):
        # -1 because of indexing in arrays
        elem = A[i] - 1
        if arr[elem] == -1:
            arr[elem] = i
    result = 0
    # loop the count array and get the max at any position
    # reason is, max at any position before x is the earliest time the frog can jump
    # if any position is not given an index, that means it does not show so return -1
    for number in arr:
        result = max(result, number)
        if number == -1:
            return number
    return result

print(solution(5, [1,3,1,4,2,3,5,4]))
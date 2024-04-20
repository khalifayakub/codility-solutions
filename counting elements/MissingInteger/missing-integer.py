# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here
    # filter to remove negative numbers, then get set of numbers and then sort
    arr = sorted(set(list(filter(lambda x : x > 0, A))))
    if len(arr) == 0:
        return 1
    # track max number
    n = float('-inf')
    for number in arr:
        n = max(n, number)
    # find the missing element
    for i in range(1,n+1):
        if arr[i-1] != i:
            return i
    # if not found from the loop, that means there is no missing number
    # and result is max + 1
    return n + 1

print(solution([-2,-3,-2]))
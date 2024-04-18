# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, k):
    n = len(A)
    if n == 0:
        return A
    k = k % n
    if k > n:
        return A
    # O(k) space complexity, this array will hold k elements so it is initialized
    temp_array = [0] * k
    # saving the last k elements into the temp array
    for i in range(n - k, n):
        temp_array[i - n + k] = A[i]
    # moving elements from start to k
    for i in range(n-k-1,-1,-1):
        A[i+k] = A[i]
    # adding the k elements to the main array
    for i in range(k):
        A[i] = temp_array[i]

    return A

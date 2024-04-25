# Let B = b * M and
#    A = a * M
# The count of numbers divisible by
# 'M' between A and B will be equal
# to b - a.

def solution(A, B, K):
    
    # Add 1 explicitly as A is divisible by K
    if (A % K == 0):
        return ((B // K) - (A // K)) + 1
    # A is not divisible by K
    return ((B // K) - (A // K))



print(solution(6,11,2))
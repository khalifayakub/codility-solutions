def solution(A: list):
    A.sort()
    N = len(A)
    # Maximal product of a triplet
    max_product = float('-inf')

    # Check two potential cases:
    # 1. Product of the last three elements
    product1 = A[N-1] * A[N-2] * A[N-3]
    # 2. Product of the first two elements and the last element
    product2 = A[0] * A[1] * A[N-1]

    # Return the maximum of the two products
    max_product = max(product1, product2)
    
    return max_product

A = [-5, 5, -5, 4]
print(solution(A))
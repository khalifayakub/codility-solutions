def solution(A):
    N = len(A)
    prefix_sum = [0] * (N + 1)
    
    # Compute prefix sums
    for i in range(1, N + 1):
        prefix_sum[i] = prefix_sum[i - 1] + A[i - 1]
    
    min_start_index = 0
    min_avg = float('inf')
    
    # Iterate through all possible starting positions P
    for P in range(N - 1):
        # Check average of slice of length 2
        avg2 = (prefix_sum[P + 2] - prefix_sum[P]) / 2.0
        if avg2 < min_avg:
            min_avg = avg2
            min_start_index = P
        
        # Check average of slice of length 3
        if P + 2 < N:
            avg3 = (prefix_sum[P + 3] - prefix_sum[P]) / 3.0
            if avg3 < min_avg:
                min_avg = avg3
                min_start_index = P
    
    return min_start_index

print(solution([-3, -5, -8, -4, -10]))
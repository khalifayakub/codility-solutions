def solution(A):
    N = len(A)
    # Calculate total sum of array
    total_sum = sum(A)
    # Initialize left sum and min difference
    left_sum = 0
    min_diff = float('inf')
    # Iterate over possible split points
    for P in range(1, N):
        left_sum += A[P-1]  # Add A[P-1] to left_sum (element just before P)
        right_sum = total_sum - left_sum  # Calculate right sum
        # Calculate absolute difference
        current_diff = abs(left_sum - right_sum)
        # Update minimum difference found
        min_diff = min(current_diff, min_diff)
    return min_diff

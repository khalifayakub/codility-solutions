# def solution(A):
#     # using built in functions
#     return len(list(set(A)))

# using count sort
def solution(A):
    if not A:
        return 0
    # Determine the range of possible values in array A
    min_value = float('inf')
    max_value = float('-inf')
    
    for num in A:
        min_value = min(num, min_value)
        max_value = max(num, max_value)
            
    # Determine the size of the counting array
    count_size = max_value - min_value + 1
    
    # Initialize counting array with zeros
    count = [0] * count_size
    
    # Populate counting array
    for num in A:
        count[num - min_value] += 1
    
    # Count distinct values
    distinct_count = 0
    for c in count:
        if c > 0:
            distinct_count += 1
    
    return distinct_count

# Test the function with the given test case
A = []
print(solution(A))  # Output: 3

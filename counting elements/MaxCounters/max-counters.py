# non efficient solution O(n*m)
# def solution(N,A):
#     result = [0] * N
#     maxi = 0
#     for number in A:
#         if number > N:
#             for i in range(N):
#                 result[i] = maxi
#         else:
#             result[number - 1] += 1
#             maxi = max(maxi, result[number - 1])
#     print(result)
#     return result

# efficient solution O(n + m)
def solution(N, A):
    # store the counts of each number
    counters = [0] * N
    # keeps track of the latest max
    max_counter = 0
    # keeps track of the last executed max counter
    last_max = 0
    
    for value in A:
        if 1 <= value <= N:
            index = value - 1
            # Lazy evaluation for increase(X) operation
            if last_max > 0 and counters[index] < last_max:
                counters[index] = last_max + 1
            else:
                counters[index] += 1
            # Update max_counter if necessary
            if counters[index] > max_counter:
                max_counter = counters[index]
        # If the operation is max counter (N + 1)
        elif value == N + 1:
            last_max = max_counter
    # Final transformation to ensure all counters are at least last_max
    for i in range(N):
        if counters[i] < last_max:
            counters[i] = last_max

    return counters

solution(5, [3,4,4,6,1,4,4])
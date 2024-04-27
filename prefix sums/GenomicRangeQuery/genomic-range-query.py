def solution(S, P, Q):
    N = len(S)
    M = len(P)
    
    # Define impact factors
    impact_factors = {'A': 1, 'C': 2, 'G': 3, 'T': 4}
    
    # Create prefix count arrays for each nucleotide type
    prefix_counts = {
        'A': [0] * (N + 1),
        'C': [0] * (N + 1),
        'G': [0] * (N + 1),
        'T': [0] * (N + 1)
    }
    
    # Fill the prefix counts arrays
    for i in range(N):
        for nucleotide in 'ACGT':
            prefix_counts[nucleotide][i + 1] = prefix_counts[nucleotide][i]
        prefix_counts[S[i]][i + 1] += 1
    
    # Answer queries
    result = []
    for k in range(M):
        start = P[k]
        end = Q[k]
        
        # Determine minimal impact factor in the range [start, end]
        if prefix_counts['A'][end + 1] - prefix_counts['A'][start] > 0:
            result.append(1)
        elif prefix_counts['C'][end + 1] - prefix_counts['C'][start] > 0:
            result.append(2)
        elif prefix_counts['G'][end + 1] - prefix_counts['G'][start] > 0:
            result.append(3)
        else:
            result.append(4)
    
    return result

print(solution("CAGCCTA", [2,5,0], [4,5,6]))
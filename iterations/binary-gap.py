# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    # Implement your solution here
    temp = 0
    ans = 0
    binary = get_binary(N)
    for number in binary:
        if number == '1':
            ans = max(ans,temp)
            temp = 0
        if number == '0':
            temp += 1
    return ans

def get_binary(N):
    return bin(N)[2:]
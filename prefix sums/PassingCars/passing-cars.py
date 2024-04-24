def solution(A):
    # keep track of vehicles coming from the west
    zeros = 0
    # result variable
    result = 0
    for number in A:
        # if the vehicle is coming from the west, keep count
        if number == 0:
            zeros += 1
        else:
        # when you see a vehicle coming from east, it is just to assume the west 
        # vehicles passed that one vehicle
            result += zeros
    
    return -1 if result > 1000000000 else result


print(solution([0,1,0,1,1]))
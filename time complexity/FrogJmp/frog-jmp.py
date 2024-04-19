def solution(X,Y,D):
    # edge case: frog is already on the target
    if X >= Y:
        return 0
    # by removing Y from X, you will have the distance the frog needs to cover
    # Dividing the distance by that should give you the amount of steps the frog needs
    # to take to reach the target
    remainder = (Y-X) % D
    steps = (Y-X) // D
    # if there's a remainder, one more jump is needed
    if remainder > 0:
        return steps + 1
    return steps
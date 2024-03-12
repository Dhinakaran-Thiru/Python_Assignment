def second_largest():
    n = 6
    array=[1,23,5,6,84,43]
    #array = map(int, input().split())
    return sorted(set(array))[-2]
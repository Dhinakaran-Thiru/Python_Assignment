def second_largest():
    n =int(input())
    array=map(int, input().split())
    #array = map(int, input().split())
    return sorted(set(array))[-2]
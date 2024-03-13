def mean_variable():
    import numpy as np
    a, b = map(int, input().split())
    l = []
    for i in range(b):
        element = list(map(int, input().split()))
        l.append(element)
    array = np.array(l)
    res=str(np.mean(array,axis=1))+"\n"+str(np.var(array,axis=0))+"\n"+str(round(np.std(array,axis=None),11))
    return res
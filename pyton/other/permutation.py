import itertools

def P0(array,count):
    return list(itertools.permutations(array,count))

def P1(array,count):
    return list(itertools.permutations(array,count))

def C2(array,count):
    return list(itertools.combinations(array,count))

def C3(array,count):
    return list(itertools.permutations(array,count))

print(P0([1,2,3,4],4))

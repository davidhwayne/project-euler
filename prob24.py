import time 

def permutation(s):
    if len(s)<=1:
        return [s]
    permutations = []
    for l in s:
        subpermut = permutation(s.replace(l, ""))
        for permut in subpermut:
            permutations.append(l + permut)
    return permutations

def getpermutationnumber(permutations,num):
    permutations.sort()
    return permutations[num-1]

def main():
    start=time.time()
    answer=getpermutationnumber(permutation('0123456789'),1000000)
    elapsed=time.time()-start
    print answer
    print 'Completed in {elapsed} seconds'.format(elapsed=elapsed)
    return True
    
main()
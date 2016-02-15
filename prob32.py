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

def sumpanprods(digits):
    s9=permutation(digits)
    panprod=[]
    for i in s9:
        if (int(i[0])*int(i[1:4])==int(i[4:])) and (int(i[4:]) not in panprod):
            panprod.append(int(i[4:]))
        elif (int(i[0])*int(i[1:5])==int(i[5:])) and (int(i[5:]) not in panprod):
            panprod.append(int(i[5:]))
        elif (int(i[0:2])*int(i[2:5])==int(i[5:])) and (int(i[5:]) not in panprod):
            panprod.append(int(i[5:]))
    return sum(panprod)
    
def main():
    start=time.time()
    answer=sumpanprods('123456789')
    elapsed=time.time()-start
    print answer
    print 'Completed in {elapsed} seconds'.format(elapsed=elapsed)
    return True
    
main()
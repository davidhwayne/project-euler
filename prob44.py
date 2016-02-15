import time
from math import sqrt

def pent(x):
    return (x*(3*x-1))/2

def ispent(a):
    solution=(1+sqrt(1+24*(a)))/6
    return int(solution)==solution
    
def minpentpair():
    current=(0,0)
    pentagonals=[]
    i=2
    while current==(0,0) or m<current[0]+current[1]:
        m=pent(i)
        pentagonals.append(m)
        for n in pentagonals:
            if ispent(m-n) and ispent(m+n):
                if current==(0,0) or (current[0]+current[1]>m+n):
                    current=(m,n)
        i+=1
    return current

def main():
    start=time.time()
    pair=minpentpair()
    answer=pair[0]-pair[1]
    elapsed=time.time()-start
    print answer
    print 'Completed in {elapsed} seconds'.format(elapsed=elapsed)
    return True
    
main()
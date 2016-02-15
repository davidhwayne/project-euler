import time
from math import sqrt

def istri(num):
    t=(-1+sqrt(1+8*num))/2
    return t==int(t)
    
def ispent(num):
    solution=(1+sqrt(1+24*(num)))/6
    return int(solution)==solution  
    
def hex(n):
    return n*(2*n-1)

def findnext(start):
    i=start
    while True:
        i+=1
        h=hex(i)
        if istri(h) and ispent(h):
            return h
            
def main():
    start=time.time()
    answer=findnext(143)
    elapsed=time.time()-start
    print answer
    print 'Completed in {elapsed} seconds'.format(elapsed=elapsed)
    return True
    
main()
        


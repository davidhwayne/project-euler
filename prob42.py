import time
from math import sqrt

def importdata(filename):
    with open(filename,'r') as f:
        data=f.read().replace('"','').split(',')
    return data
    
def computescore(word):
    alphaval = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}
    return sum([alphaval[w] for w in word])

def istri(num):
    t=(-1+sqrt(1+8*num))/2
    return t==int(t)
    
def triwords(words):
    return sum([1 for w in words if istri(computescore(w))])
    
def main():
    start=time.time()
    answer=triwords(importdata('p042_words.txt'))
    elapsed=time.time()-start
    print answer
    print 'Completed in {elapsed} seconds'.format(elapsed=elapsed)
    return True
    
main()
        
    

import time

def importdata(filename):
    with open(filename,'r') as f:
        names=f.read().replace('"','').split(',')
        names.sort()
    return names

def alphascore(namelist):
    alphaval = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}
    return sum([sum([alphaval[l] for l in name])*(i+1) for i,name in enumerate(namelist)])
         
def main():
    start=time.time()
    answer=alphascore(importdata('p022_names.txt'))
    elapsed=time.time()-start
    print answer
    print 'Completed in {elapsed} seconds'.format(elapsed=elapsed)
    return True
    
main()
        

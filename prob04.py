import time

def ispalindrome(n):
    stringn=str(n)
    l=len(stringn)
    for i in range(0,l/2+1):
        if stringn[i]!=stringn[l-i-1]:
            return False    
            break
    else:
        return True

def largestpalinprod(maxval):
    current=1
    for i in range(maxval)[::-1]:
        for j in range(maxval)[::-1]:
            if ispalindrome(i*j) and i*j>current:
                current=i*j
    return current        
    
def main():
    start=time.time()
    answer=largestpalinprod(1000)
    elapsed=time.time()-start
    print answer
    print 'Completed in {elapsed} seconds'.format(elapsed=elapsed)
    return True

main()
    

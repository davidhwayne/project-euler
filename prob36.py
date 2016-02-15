import time

def ispalindrome(s):
    l=len(s)
    for i in range(l/2):
        if s[i]!=s[l-i-1]:
            return False
            break
    else:
        return True

def sumpalindromes():
    return sum([i for i in range(1,1000000) if ispalindrome(str(i)) and ispalindrome(bin(i)[2:])])

    
def main():
    start=time.time()
    answer=sumpalindromes()
    elapsed=time.time()-start
    print answer
    print 'Completed in {elapsed} seconds'.format(elapsed=elapsed)
    return True
    
main()
       
    
    
    

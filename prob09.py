import time

def triplediv(n):
    primitives=[[3, 4, 5],[5, 12, 13],[8, 15, 17],[7, 24, 25],[20, 21, 29],[12, 35, 37],[9, 40, 41],[28, 45, 53],[11, 60, 61],[16, 63, 65],[33, 56, 65],[48, 55, 73],[13, 84, 85],[36, 77, 85],[39, 80, 89],[65, 72, 97]]
    for p in primitives:
        s=sum(p)
        if n%s==0:
            return p[0]*p[1]*p[2]*(n/s)**3
            
def main():
    start=time.time()
    answer=triplediv(1000)
    elapsed=time.time()-start
    print answer
    print 'Completed in {elapsed} seconds'.format(elapsed=elapsed)
    return True
    
main()
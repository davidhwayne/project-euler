import time

def by17():
    return ['0'+str(17*i) for i in range(1,6)]+[str(17*i) for i in range(6,59) if len(set(str(17*i)))==3]

def by13():
    return ['0'+str(13*i) for i in range(1,8)]+[str(13*i) for i in range(8,77) if len(set(str(13*i)))==3]
    
def by11():
    return ['0'+str(11*i) for i in range(1,10)]+[str(11*i) for i in range(10,91) if len(set(str(11*i)))==3]
    
def by7():
    return ['0'+str(7*i) for i in range(1,15)]+[str(7*i) for i in range(15,143) if len(set(str(7*i)))==3]
    
def by5():
    return ['0'+str(5*i) for i in range(1,20)]+[str(5*i) for i in range(20,200) if len(set(str(5*i)))==3]
    
def by3():
    return ['0'+str(3*i) for i in range(1,34)]+[str(3*i) for i in range(34,334) if len(set(str(3*i)))==3]
    
def by2():
    return ['0'+str(2*i) for i in range(1,50)]+[str(2*i) for i in range(50,500) if len(set(str(2*i)))==3]
    
def possiblepans():
    possibles=[]
    for d10 in by17():
        for d9 in by13():
            if d9[1:]==d10[:2]:
                for d8 in by11():
                    if d8[1:]==d9[:2]:
                        for d7 in by7():
                            if d7[1:]==d8[:2]:
                                for d6 in by5():
                                    if d6[1:]==d7[:2]:
                                        for d5 in by3():
                                            if d5[1:]==d6[:2]:
                                                for d4 in by2():
                                                    if d4[1:]==d5[:2]:
                                                        possibles.append(d4+d7+d10)
    return possibles

def completepan(p):
    if len(set(p))==9:
        for element in set([str(i) for i in range(10)])-set(p):
            d1=element
        return int(str(d1)+p)
    else:
        return 0
        
def sumpans():
    return sum([completepan(p) for p in possiblepans()])
    
def main():
    start=time.time()
    answer=sumpans()
    elapsed=time.time()-start
    print answer
    print 'Completed in {elapsed} seconds'.format(elapsed=elapsed)
    return True
    
main()
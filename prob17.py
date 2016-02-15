import time

def countletters():
    single="onetwothreefourfivesixseveneightnine"
    teen="teneleventwelvethirteenfourteenfifteensixteenseventeeneighteennineteen"
    double="twentythirtyfortyfiftysixtyseventyeightyninety"
    triple="hundred"
    sum=10*(len(single) + len(teen) + 10*len(double) + 8*len(single)) + 900*(len(triple)) + 100*len(single) + 891*len('and') + len('onethousand')
    return sum

def main():
    start=time.time()
    answer=countletters()
    elapsed=time.time()-start
    print answer
    print 'Completed in {elapsed} seconds'.format(elapsed=elapsed)
    return True
    
main()
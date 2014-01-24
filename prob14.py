most=0
current=1
for n in range(1,1000000):
	count=0
	i=n
	while i!=1:
		count=count+1
		if i%2==0:
			i=i/2
		else:
			i=3*i+1
	if count>most:
		most=count
		current=n
print 
print 'Number of iterations = '+str(most)
print 'For the number: '+str(current)
			

def isab(n):
	divisors=[]
	for j in range(1,n):
		if n%j==0:
			divisors.append(j)
	sumdiv=sum(divisors)
	if n<sumdiv:
		return True
	else:
		return False

print "Finding abundants..."
abs=[]
for i in range(1,28123):
	if isab(i):
		abs.append(i)

print "Sum abundants..."
sums=[]
for i in range(len(abs)):
	for j in range(i,len(abs)):
		sums.append(abs[i]+abs[j])

print "Sort summed abundants..."
sums.sort()

print "Sum non-abundant-sums..."
total=0
j=0
for i in range(1,28123):
	while i>=sums[j]:
		if i==sums[j]:
			break
		else:
			j=j+1
	else:
		total=total+i

print total



def ispan(n):
	s=list(n)
	s.sort()
	for i in range(9):
		if str(i+1)!=s[i]:
			return False
			break
	else:
		return True
print ispan('123456789')
print ispan('213457698')
print ispan('nope')



current=918273645
k=0
for i in range(9487,9233,-1):
	new=str(i)+str(i*2)
	if ispan(new) and int(new)>current:
		print new
		break







def ispalindrome(n):
	stringn=str(n)
	l=len(stringn)
	for i in range(0,l/2+1):
		if stringn[i]!=stringn[l-i-1]:
			return False	
			break
	else:
		return True

current=1
for i in range(1000)[::-1]:
	for j in range(1000)[::-1]:
		if ispalindrome(i*j) and i*j>current:
			current=i*j
print current		
	
	

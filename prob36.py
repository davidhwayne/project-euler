def ispalindrome(s):
	l=len(s)
	for i in range(l/2):
		if s[i]!=s[l-i-1]:
			return False
			break
	else:
		return True

sum=0
for i in range(1,1000000):
	decimal=str(i)
	binary=bin(i)[2:]
	if ispalindrome(decimal) and ispalindrome(binary):
		sum=sum+i
print sum
	
	
	

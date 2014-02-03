alphaval = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}
nametxt=open('names.txt','r')
names=nametxt.read()
namelist=names.split('","')
namelist[0]=namelist[0][1:]
namelist[-1]=namelist[-1][:-1]
namelist.sort()
print namelist[0]

sum=0
i=1
for name in namelist:
	namesum=0
	for l in name:
		namesum=namesum+alphaval[l]
	sum=sum+namesum*i
	i=i+1

print sum
		

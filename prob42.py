alphaval = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}
wordtxt=open('words.txt','r')
words=wordtxt.read()
wordlist=words.split('","')
wordlist[0]=wordlist[0][1:]
wordlist[-1]=wordlist[-1][:-1]

scores=[]
for i in wordlist:
	score=0
	for j in i:
		score=score+alphaval[j]
	scores.append(score)

tri=[]
for i in range(1,21):
	tri.append((i*(i+1))/2)

count=0
for s in scores:
	if s in tri:
		count+=1
print count
	

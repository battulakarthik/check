 def hun_33():
	s=input()
	i,b,c=0,0,0
	while(i<len(s)):
		if(b==0):
			if(s[i]=='a'):
				c+=1
				i+=1
				b=1
			continue
		if(b==1):
			if(s[i]=='b'):
				c+=1
				i+=1
				b=0
	print(c)
try:
	hun_33()
except:
	print('Invalid')

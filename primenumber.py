# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
arr=[]
for i in range(10):
	flag=1
	if i<=1:
		flag=0		
	else:
		for j in range(2,(i//2)+1):
            
			if i%j==0:
				flag=0
	if flag==1:
		arr.append(i)

print(arr)
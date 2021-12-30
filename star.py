def part(n):
	for i in range(0,n):
    	for j in range(0,i+1):#nested looping
        	print("*",end="")    
		print("\r")#two dimensional array printing,nested loop
n=5
part(n)

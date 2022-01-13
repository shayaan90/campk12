rows=5
b=0

for i in range(rows,0,-1):
  b+=1
  for j in range(1,i+1):#nested looping
    print(b,end="")    
  print("\r")#to print in new line 

#drawing pattern triangle 
#first loop downwards(rows) then second loop sidewards (columns)
def triangle(n):
  k=n-1#for upside triangle remove this
  for i in range(0,n): #outer loop handling rows
    for j in range(0,k):#remove k for upside triangle and add n(0,1)
      print(end=" ")
    k=k-1#remove this
    for j in range(0,i+1):
      print("1 ",end="")
    print("\r") #enter new line
n=5
triangle(n)#closing function

n=8
m=n+1#coluns

#upper Part
for i in range(n//2-1):
  for j in range(m):
    if i==n//2-2 and (j==0 or j==m-1):
      print("* ",end=" ")
    elif j<=m//2 and ((i+j==n//2-3 and j<=m//4) \ or (j-i==m//2-n//2+3 and j>m//4)):#nested loop
      print("* ",end=" ")#printing stars left upper side
    elif j>m//2 and ((i+j==n//2-3+m//2 and j<3*m//4) \ or (j-i==m//2-n//2+3+m//2 and j>3*m//4)):#nested condition
      print("* ",end=" ")#printing stars right upper side, j= only in one condition

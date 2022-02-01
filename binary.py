print("this is binary search")
def binarysearchAppr (arr, start, end, x):
  if end >= start:
     mid = start + (end- start)//2
     if arr[mid] == x:
       return mid
     elif arr[mid] > x:
       return binarysearchAppr(arr, start, mid-1, x)
     else:
       return binarysearchAppr(arr, mid+1, end, x)
  else:
    return -1
arr = sorted(['i','m','a','t','r','e','e'])
x =input("enter the element to search: ")
result = binarysearchAppr(arr, 0, len(arr)-1, x)
if result != -1:
  print ("element is present at index "+str(result))
else:
  print ("element is not present in array")          

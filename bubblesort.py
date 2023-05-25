import time
def bubblesort(arr):
          n=len(arr)
          swapped=False
          #traverse through all array elements
          for i in range(n-1):
               for j in range(0,n-i-1):

                    #traverse the array from 0 to n-i-1
                    #swap if the element found is greater
                    #than the next element
                    if arr[j]>arr[j+1]:
                         swapped=True
                         arr[j],arr[j+1]=arr[j+1],arr[j]
          if not swapped:
               return
#driver code to test above
arr=[64,34,25,12,22,11,90]
st=time.time()
bubblesort(arr)
et=time.time()
etime=st-et
print("Execution time=",etime)
print("sorted array is:")
for i in range(len(arr)):
     print("%d"%arr[i],end=" ")
                         

def bubble(arr,n):
    if n==0 or n==1:
        return arr
    for i in range(n-1):
        if arr[i+1]<arr[i]:
            arr[i+1],arr[i]=arr[i],arr[i+1]
            
    return bubble(arr,n-1)
print(bubble([3,2,1,6,5,4],6))

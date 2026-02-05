# defining function 
def leastnumber_k(arr, k):
    #sorting array
    arr.sort()
    return arr[k - 1]
#defining array
arr = [10, 5, 4, 3, 48, 6, 2, 33, 53, 10]
k = 4
print(leastnumber_k(arr, k))

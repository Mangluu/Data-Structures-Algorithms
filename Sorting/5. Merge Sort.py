def merge_sorted(arr1, arr2):
    sorted_arr = []
    i , j = 0 , 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            sorted_arr.append(arr1[i])
            i += 1
        else:
            sorted_arr.append(arr2[j])
            j += 1

    if i < len(arr1):
        sorted_arr += arr1[i:]

    if j < len(arr2):
        sorted_arr += arr2[j:]

    return sorted_arr

def divide_arr(arr):
    if len(arr) < 2:
        return arr[:]
    else:
        middle = len(arr)//2
        l1 = divide_arr(arr[:middle])
        l2 = divide_arr((arr[middle:]))
        return merge_sorted(l1, l2)


l = [1,4,6,2,3,5,7,8,9,8,10]
print(divide_arr(l))

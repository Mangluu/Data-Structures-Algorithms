def binary_search(arr, num):
    low = 0
    high = len(arr) - 1

    while high >= low:
        mid = (low + high)//2
        if num == arr[mid]:
            print(num, "found at position", mid + 1)
            return
        elif num > arr[mid]:
            low = mid + 1
        else:
            high = mid - 1
    print(num, "not found in list")
    return


arr = sorted([i for i in range(1, 100)])
binary_search(arr, 99)

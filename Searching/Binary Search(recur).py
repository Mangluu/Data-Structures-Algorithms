def binary_search(arr, num, low, high):
    if low > high:
        print(num, "not found in list")
        return

    mid = (low + high)//2

    if num == arr[mid]:
        print(num, "found at position", mid + 1)
        return
    elif num > arr[mid]:
        return binary_search(arr, num, mid + 1, high)
    else:
        return binary_search(arr, num, low, mid - 1)


arr = sorted([i for i in range(1, 100)])
binary_search(arr, 99, 0, len(arr))

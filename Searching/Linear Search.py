def linear_search(arr, num):
    for i in range(len(arr)):
        if arr[i] == num:
            print(num, "found at position", i + 1)
            return
    print(num, "not found in list")
    return


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
linear_search(arr, 5)

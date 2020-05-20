def insertion_sort(arr):
    for i in range(1, len(arr)):
        print(arr)
        for j in range(i,0,-1):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]

    print(arr)
    return

l = [6, 1, 8, 4, 10]
insertion_sort(l)

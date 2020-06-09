def bubble_sort(arr):
    for j in range(len(arr)-1, 1, -1):
        print(arr)
        for i in range(0, j):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
    return


l = [6, 8, 1, 4, 10, 7, 8, 9, 3, 2, 5]
bubble_sort(l)

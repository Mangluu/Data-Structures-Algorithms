def selection_sort(arr):
    for i in range(len(arr)):
        print(arr)
        for j in range(i, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]


l = [6, 8, 1, 4, 10, 7, 8, 9, 3, 2, 5]
selection_sort(l)

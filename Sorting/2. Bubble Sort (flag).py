def bubble_sort(arr):
    swap_status = True
    for j in range(len(arr)-1, 0, -1):
        if swap_status == False:
            break
        swap_status = False
        print(arr)
        for i in range(0, j):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swap_status = True
    return


l = [6, 8, 1, 4, 10, 7, 8, 9, 3, 2, 5]
bubble_sort(l)

def insertion_sort(arr):
    for key in range(1, len(arr)):
        if arr[key] < arr[key-1]:
            j = key
            while j > 0 and arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
                j -= 1

l = [6, 8, 1, 4, 10, 7, 8, 9, 3, 2, 5]
insertion_sort(l)
print(l)

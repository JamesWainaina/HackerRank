#!/usr/bin/python3

def cyclic_sort(arr):
    i = 0
    while i < len(arr):
        correct = arr[i] - 1
        if 0 <= correct < len(arr) and arr[i] != arr[correct]:
            arr[i], arr[correct] = arr[correct], arr[i]
        else:
            i += 1


if __name__ == "__main__":
    array = [3, 1, 5, 4, 2]
    cyclic_sort(array)
    print("Sorted array:", array)
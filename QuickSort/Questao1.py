import random;


def quicksort(array, left=0, right=None):
    if right is None:
        right=len(array)-1
    if left < right:
        pivot_index = partition(array, left, right)
        quicksort(array, left, pivot_index - 1)
        quicksort(array, pivot_index + 1, right)



def partition(array, left, right):
    pivot = array[right]
    i = left - 1

    for j in range(left, right):
        if array[j] >= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]

    array[i + 1], array[right] = array[right], array[i + 1]
    return i + 1


array = [random.randint(1, 100) for _ in range(10)]
print(array)
quicksort(array)
print(array)
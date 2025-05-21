import random
def merge_sort_maisum(arr):
    if len(arr) <= 1:
        return arr

    mid = (len(arr)+1) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    sorted_left = merge_sort_maisum(left_half)
    sorted_right = merge_sort_maisum(right_half)

    return merge(sorted_left, sorted_right)

def merge_sort_menosum(arr):
    if len(arr) <= 1:
        return arr

    mid = (len(arr)-1) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    sorted_left = merge_sort_menosum(left_half)
    sorted_right = merge_sort_menosum(right_half)

    return merge(sorted_left, sorted_right)


def merge(a, b):
    i = 0
    j = 0
    c = [] 

    
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            c.append(a[i]) 
            i += 1
        else:
            c.append(b[j])
            j += 1

    
    while i < len(a):
        c.append(a[i])
        i += 1

    
    while j < len(b):
        c.append(b[j])
        j += 1

    return c 

array = [random.randint(1, 1000) for _ in range(8)]
array = merge_sort_maisum(array)
print(array)

lista = [random.randint(1, 1000) for _ in range(8)]
lista = merge_sort_menosum(lista)
print(lista)

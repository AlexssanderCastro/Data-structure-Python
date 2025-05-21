import random


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    sorted_left = merge_sort(left_half)
    sorted_right = merge_sort(right_half)

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

#Função que confere se o merge_sort ordenou
def conferir(array):
    for i in range(1,len(array)):
        if(array[i]<array[i-1]):
            print("Não está ordenado")
            return
    print("Está ordenado")

array = [random.randint(1, 10000) for _ in range(1000)]
array=merge_sort(array)
conferir(array)
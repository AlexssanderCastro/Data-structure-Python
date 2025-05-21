def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    sorted_left = merge_sort(left_half)
    sorted_right = merge_sort(right_half)

    return merge(sorted_left, sorted_right)

# Retorna uma nova lista contendo os elementos de a e b em ordem
def merge(a, b):
    i = 0
    j = 0
    c = [] # Lista resultado

    # Enquanto houver elementos em ambas as listas
    while i < len(a) and j < len(b):
        if a[i] >= b[j]:
            c.append(a[i]) # Copia o menor de a ou b
            i += 1
        else:
            c.append(b[j])
            j += 1

    # Copia o restante de a (se houver)
    while i < len(a):
        c.append(a[i])
        i += 1

    # Copia o restante de b (se houver)
    while j < len(b):
        c.append(b[j])
        j += 1

    return c # Lista mesclada e ordenada


arr=[1,2,3,4,5]

print(arr)

arr=merge_sort(arr)

print(arr)
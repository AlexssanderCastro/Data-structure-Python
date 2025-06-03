def qsrt ( array , left=0 , right=None ) :
    if right is None:
        right=len(array)-1
    j = partition ( array , left , right )
    if ( left < j - 1) :
     qsrt ( array , left , j - 1)
    if ( j + 1 < right ) :
        qsrt ( array , j + 1 , right )

def partition(array, left, right):
    pivot = array[right]
    i = left - 1

    for j in range(left, right):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]

    array[i + 1], array[right] = array[right], array[i + 1]
    return i + 1

array = [3, 1, 2,5,6,1]
qsrt(array)
print(array)

# O código funciona corretamente para ordenar em todos os casos, mas colocar uma implementação
# para que não seja necessário chamar a função dando left e right na primeira vez pode tornar o 
# algoritmo bem mais prático em usabilidade

def quicksort(array, left=0, right=None):
    if right is None:
        right=len(array)-1
    if left < right:
        pivot_index = sep(array, left, right)
        quicksort(array, left, pivot_index - 1)
        quicksort(array, pivot_index + 1, right)

def sep ( array , left , right ) :
    j = right
    for i in range ( right - 1 , left - 1 , -1) :
        if array [ i ] > array [ right ]:
            array [ i ] , array [ right ] = array [ right ] , array [ i ]
            j = i
    return j

array = [3, 1, 2, 5, 6, 1]
quicksort(array)
print(array)

# A linha array[i], array[right] = array[right], array[i] 
# troca diretamente array[i] com o pivô array[right], sempre que array[i] > pivot.
#
# Isso altera a posição do pivô durante o laço, o que quebra totalmente o princípio 
# do particionamento (onde o pivô deve ficar fixo até o final). Com isso o pivô pode
# "andar" incorretamente, e o vetor pode acabar com elementos maiores misturados com os menores
# e isso acaba tornando a função inutilizável, pois não funciona para ordenar.

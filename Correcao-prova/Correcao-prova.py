#Correção da prova

# Questão 1- A lógica está quase correta, pois verifica se um número é menor que o anterior e retorna
# false caso a lista esteja desordenada, mas a variável "sim" não é declarada antes, o que vai 
# ocasionar um erro, além do que não é necessário atribuir valor a ela em toda iteração, você pode
# iniciá-la como true e mudar o valor apenas no caso de a lista estar desordenada.

def verifica(lista):
    n=len(lista)
    sim=True
    for i in range(1,n):
        if lista[i-1]>lista[i]:
            sim=False
            break
    return sim

#-----------------------------------------------------------------------------------------------------#

# Questão 2 -

def bubble_sort(array):
    tamanho = len(array)
    for i in range(tamanho):
        mudou=False
        for j in range(0, tamanho-i-1):
            if array[j]>array[j+1]:
                array[j], array[j+1]= array[j+1],array[j]
                mudou=True
        if mudou==False:
            break
     

#-----------------------------------------------------------------------------------------------------#

# Questão 3- Letra D - 16

#-----------------------------------------------------------------------------------------------------#

# Questão 4-
# 
# a)Se voce fizer essa mudança o primeiro número ficará sem ser comparado ou modificado, e a não ser 
# que ele seja já o menor número, a lista ficará sempre ordenada errado.
# 
# b)Se você fizer essa mudança você terá problemas com o tamanho da lista, pois faz a comparação do 
# número atual do index i com os próximos, além de ser completamente desnecessário, pois se o último
# número já é maior que o penúltimo, não há a necessidade de nenhuma troca.
# 
# c)Nesse caso você não teria uma alteração a lógica, mas cria uma situação desnecessária pois não é 
# preciso trocar um número por ele mesmo, mesmo que nesse caso v[min-index] fosse o menor número, um 
# número igual a ele estaria logo após ele na lista

#-----------------------------------------------------------------------------------------------------#

#Questão 5-
# 
#a)O pior caso e O(n²), pois no Selection Sort todas as comparações são feitas independente do quão
# ordenado o vetor está, pois ele percorrerá todos os números sempre da mesma forma buscando o menor,
# mas se ele estiver completamente desordenado como em [7,6,5,3,4,2,1], nem o número de trocas é 
# possível mudar.
# 
#b)O melhor caso é O(n²) também, pois mesmo que o array já esteja quase ordenado,não é possível 
# interromper o Selection Sort, ou seja, todas as comparações sempre serão feitas, o que é póssível
#  é apenas diminuir o número de trocas realizadas, como no caso [1,2,3,,5,4,6,7], onde é possível 
# reduzir o número de trocas para apenas uma, pois a lista já está quase ordenada.

#-----------------------------------------------------------------------------------------------------#

#Questão 6- O v[i] = x, é totalmente desnecessário , pois ocupa mais espaço de memória, já que se
# colocar depois de finazliar o while como v[i+1]=aux já garante a posição correta. Outro problema
# é o primeiro "for" começar com (1,n), ou seja, ignorando a primeira posição que seria o (0,n)

#-----------------------------------------------------------------------------------------------------#

#Questão 7-

def insertion_sort_recursivo(array, n=None):
    if n is None:
        n = len(array)
    if n <= 1:
        return
    insertion_sort_recursivo(array, n - 1)
    numero = array[n - 1]
    j = n - 2
    while j >= 0 and array[j] > numero:
        array[j + 1] = array[j]
        j -= 1
    array[j + 1] = numero

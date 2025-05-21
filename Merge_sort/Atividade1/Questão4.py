class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

def exibir_lista(cabeca):
    atual = cabeca
    while atual:
        print(atual.valor, end=" -> ")
        atual = atual.proximo
    print("None")

def merge_sort_lista(cabeca):
    if cabeca is None or cabeca.proximo is None:
        return cabeca

    meio = encontrar_meio(cabeca)
    proximo_do_meio = meio.proximo
    meio.proximo = None  

    esquerda = merge_sort_lista(cabeca)
    direita = merge_sort_lista(proximo_do_meio)

    return mesclar_listas(esquerda, direita)

def encontrar_meio(cabeca):
    lento = cabeca
    rapido = cabeca.proximo
    while rapido and rapido.proximo:
        lento = lento.proximo
        rapido = rapido.proximo.proximo
    return lento

def mesclar_listas(esquerda, direita):
    if esquerda is None:
        return direita
    if direita is None:
        return esquerda

    if esquerda.valor <= direita.valor:
        resultado = esquerda
        resultado.proximo = mesclar_listas(esquerda.proximo, direita)
    else:
        resultado = direita
        resultado.proximo = mesclar_listas(esquerda, direita.proximo)
    
    return resultado


n1 = No(4)
n2 = No(2)
n3 = No(1)
n4 = No(3)

n1.proximo = n2
n2.proximo = n3
n3.proximo = n4

print("Lista original:")
exibir_lista(n1)

ordenada = merge_sort_lista(n1)

print("Lista ordenada:")
exibir_lista(ordenada)

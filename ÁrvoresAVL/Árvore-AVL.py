class NoAVL:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None
        self.altura = 1

#Função para pegar a altura atual de um nó
def obter_altura(no):
    if no is None:
        return 0
    return no.altura

#Função para calcular o Fator de Balanceamento
def fator_balanceamento(no):
    if no is None:
        return 0
    return obter_altura(no.esquerda) - obter_altura(no.direita)

#Função para atualizar a altura do nó
def atualizar_altura(no):
    no.altura = 1 + max(obter_altura(no.esquerda), obter_altura(no.direita))

#Rotação a direita
def rotacao_direita(y):
    x = y.esquerda
    T2 = x.direita

    x.direita = y
    y.esquerda = T2

    atualizar_altura(y)
    atualizar_altura(x)

    return x

#Rotação a esquerda
def rotacao_esquerda(x):
    y = x.direita
    T2 = y.esquerda

    y.esquerda = x
    x.direita = T2

    atualizar_altura(x)
    atualizar_altura(y)

    return y

#Inserção de novo numero
def inserir(no, valor):
    if no is None:
        return NoAVL(valor)

    if valor < no.valor:
        no.esquerda = inserir(no.esquerda, valor)
    elif valor > no.valor:
        no.direita = inserir(no.direita, valor)
    else:
        return no  # valor duplicado não é permitido

    atualizar_altura(no)

    balanceamento = fator_balanceamento(no)

    # Casos de rotação
    if balanceamento > 1 and valor < no.esquerda.valor:
        return rotacao_direita(no)

    if balanceamento < -1 and valor > no.direita.valor:
        return rotacao_esquerda(no)

    if balanceamento > 1 and valor > no.esquerda.valor:
        no.esquerda = rotacao_esquerda(no.esquerda)
        return rotacao_direita(no)

    if balanceamento < -1 and valor < no.direita.valor:
        no.direita = rotacao_direita(no.direita)
        return rotacao_esquerda(no)

    return no

#Encontrar o menor valor da sub-arvore
def encontrar_menor_valor(no):
    atual = no
    while atual.esquerda is not None:
        atual = atual.esquerda
    return atual

#Remover um número
def remover(no, valor):
    if no is None:
        return no

    if valor < no.valor:
        no.esquerda = remover(no.esquerda, valor)
    elif valor > no.valor:
        no.direita = remover(no.direita, valor)
    else:
        if no.esquerda is None:
            return no.direita
        elif no.direita is None:
            return no.esquerda

        temp = encontrar_menor_valor(no.direita)
        no.valor = temp.valor
        no.direita = remover(no.direita, temp.valor)

    atualizar_altura(no)

    balanceamento = fator_balanceamento(no)

    # Rebalanceamentos após remoção
    if balanceamento > 1 and fator_balanceamento(no.esquerda) >= 0:
        return rotacao_direita(no)

    if balanceamento > 1 and fator_balanceamento(no.esquerda) < 0:
        no.esquerda = rotacao_esquerda(no.esquerda)
        return rotacao_direita(no)

    if balanceamento < -1 and fator_balanceamento(no.direita) <= 0:
        return rotacao_esquerda(no)

    if balanceamento < -1 and fator_balanceamento(no.direita) > 0:
        no.direita = rotacao_direita(no.direita)
        return rotacao_esquerda(no)

    return no

#Imprimir números em ordem
def imprimir_em_ordem(no):
    if no is not None:
        imprimir_em_ordem(no.esquerda)
        print(no.valor, end=' ')
        imprimir_em_ordem(no.direita)


#Main para testes
if __name__ == "__main__":
    raiz = None
    for numero in [70, 20, 1, 40, 50, 25]:
        raiz = inserir(raiz, numero)

    print("Árvore em ordem após inserções:")
    imprimir_em_ordem(raiz)
    print()

    raiz = remover(raiz, 1)
    print("Árvore em ordem após remover o 30:")
    imprimir_em_ordem(raiz)
    print()

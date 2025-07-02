VERMELHO = True
PRETO = False

class No:
    def __init__(self, valor):
        self.valor = valor
        self.cor = VERMELHO
        self.esquerda = None
        self.direita = None
        self.pai = None

class ArvoreRedBlack:
    def __init__(self):
        self.nulo = No(None)
        self.nulo.cor = PRETO
        self.nulo.esquerda = self.nulo.direita = self.nulo
        self.raiz = self.nulo

    def buscar(self, valor):
        return self._buscar(self.raiz, valor)

    def _buscar(self, no, valor):
        if no == self.nulo or valor == no.valor:
            return no
        if valor < no.valor:
            return self._buscar(no.esquerda, valor)
        else:
            return self._buscar(no.direita, valor)

    def rotacionar_esquerda(self, no):
        direita = no.direita
        no.direita = direita.esquerda
        if direita.esquerda != self.nulo:
            direita.esquerda.pai = no
        direita.pai = no.pai
        if no.pai == None:
            self.raiz = direita
        elif no == no.pai.esquerda:
            no.pai.esquerda = direita
        else:
            no.pai.direita = direita
        direita.esquerda = no
        no.pai = direita

    def rotacionar_direita(self, no):
        esquerda = no.esquerda
        no.esquerda = esquerda.direita
        if esquerda.direita != self.nulo:
            esquerda.direita.pai = no
        esquerda.pai = no.pai
        if no.pai == None:
            self.raiz = esquerda
        elif no == no.pai.direita:
            no.pai.direita = esquerda
        else:
            no.pai.esquerda = esquerda
        esquerda.direita = no
        no.pai = esquerda

    def inserir(self, valor):
        novo = No(valor)
        novo.esquerda = novo.direita = self.nulo
        pai = None
        atual = self.raiz

        while atual != self.nulo:
            pai = atual
            if novo.valor < atual.valor:
                atual = atual.esquerda
            else:
                atual = atual.direita

        novo.pai = pai
        if pai == None:
            self.raiz = novo
        elif novo.valor < pai.valor:
            pai.esquerda = novo
        else:
            pai.direita = novo

        novo.cor = VERMELHO
        self._corrigir_insercao(novo)

    def _corrigir_insercao(self, no):
        while no.pai and no.pai.cor == VERMELHO:
            if no.pai == no.pai.pai.esquerda:
                tio = no.pai.pai.direita
                if tio.cor == VERMELHO:
                    no.pai.cor = PRETO
                    tio.cor = PRETO
                    no.pai.pai.cor = VERMELHO
                    no = no.pai.pai
                else:
                    if no == no.pai.direita:
                        no = no.pai
                        self.rotacionar_esquerda(no)
                    no.pai.cor = PRETO
                    no.pai.pai.cor = VERMELHO
                    self.rotacionar_direita(no.pai.pai)
            else:
                tio = no.pai.pai.esquerda
                if tio.cor == VERMELHO:
                    no.pai.cor = PRETO
                    tio.cor = PRETO
                    no.pai.pai.cor = VERMELHO
                    no = no.pai.pai
                else:
                    if no == no.pai.esquerda:
                        no = no.pai
                        self.rotacionar_direita(no)
                    no.pai.cor = PRETO
                    no.pai.pai.cor = VERMELHO
                    self.rotacionar_esquerda(no.pai.pai)
        self.raiz.cor = PRETO

    def _transplantar(self, u, v):
        if u.pai == None:
            self.raiz = v
        elif u == u.pai.esquerda:
            u.pai.esquerda = v
        else:
            u.pai.direita = v
        v.pai = u.pai

    def _minimo(self, no):
        while no.esquerda != self.nulo:
            no = no.esquerda
        return no

    def remover(self, valor):
        no = self.buscar(valor)
        if no == self.nulo:
            print(f"Valor {valor} não encontrado para remoção.")
            return

        original_cor = no.cor
        if no.esquerda == self.nulo:
            substituto = no.direita
            self._transplantar(no, no.direita)
        elif no.direita == self.nulo:
            substituto = no.esquerda
            self._transplantar(no, no.esquerda)
        else:
            minimo = self._minimo(no.direita)
            original_cor = minimo.cor
            substituto = minimo.direita
            if minimo.pai == no:
                substituto.pai = minimo
            else:
                self._transplantar(minimo, minimo.direita)
                minimo.direita = no.direita
                minimo.direita.pai = minimo
            self._transplantar(no, minimo)
            minimo.esquerda = no.esquerda
            minimo.esquerda.pai = minimo
            minimo.cor = no.cor

        if original_cor == PRETO:
            self._corrigir_remocao(substituto)

    def _corrigir_remocao(self, no):
        while no != self.raiz and no.cor == PRETO:
            if no == no.pai.esquerda:
                irmao = no.pai.direita
                if irmao.cor == VERMELHO:
                    irmao.cor = PRETO
                    no.pai.cor = VERMELHO
                    self.rotacionar_esquerda(no.pai)
                    irmao = no.pai.direita
                if irmao.esquerda.cor == PRETO and irmao.direita.cor == PRETO:
                    irmao.cor = VERMELHO
                    no = no.pai
                else:
                    if irmao.direita.cor == PRETO:
                        irmao.esquerda.cor = PRETO
                        irmao.cor = VERMELHO
                        self.rotacionar_direita(irmao)
                        irmao = no.pai.direita
                    irmao.cor = no.pai.cor
                    no.pai.cor = PRETO
                    irmao.direita.cor = PRETO
                    self.rotacionar_esquerda(no.pai)
                    no = self.raiz
            else:
                irmao = no.pai.esquerda
                if irmao.cor == VERMELHO:
                    irmao.cor = PRETO
                    no.pai.cor = VERMELHO
                    self.rotacionar_direita(no.pai)
                    irmao = no.pai.esquerda
                if irmao.direita.cor == PRETO and irmao.esquerda.cor == PRETO:
                    irmao.cor = VERMELHO
                    no = no.pai
                else:
                    if irmao.esquerda.cor == PRETO:
                        irmao.direita.cor = PRETO
                        irmao.cor = VERMELHO
                        self.rotacionar_esquerda(irmao)
                        irmao = no.pai.esquerda
                    irmao.cor = no.pai.cor
                    no.pai.cor = PRETO
                    irmao.esquerda.cor = PRETO
                    self.rotacionar_direita(no.pai)
                    no = self.raiz
        no.cor = PRETO

    def _em_ordem(self, no):
        if no != self.nulo:
            self._em_ordem(no.esquerda)
            cor = "(V)" if no.cor else "(P)"
            print(f"{no.valor} {cor}", end=" ")
            self._em_ordem(no.direita)

    def mostrar_em_ordem(self):
        print("Elementos em ordem (com cor):")
        self._em_ordem(self.raiz)
        print()


if __name__ == "__main__":
    arvore = ArvoreRedBlack()
    for numero in [20, 15, 25, 10, 5, 1, 30]:
        arvore.inserir(numero)

    arvore.mostrar_em_ordem()

    print("\nRemovendo 10...")
    arvore.remover(10)
    arvore.mostrar_em_ordem()

    print("\nRemovendo 25...")
    arvore.remover(25)
    arvore.mostrar_em_ordem()

    print("\nRemovendo 15...")
    arvore.remover(15)
    arvore.mostrar_em_ordem()

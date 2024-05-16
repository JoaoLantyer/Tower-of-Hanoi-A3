movimentos = []

class Pilha:
    def __init__(self):
        self.itens = []

    def empilhar(self, x):
        self.itens.append(x)

    def desempilhar(self):
        if len(self.itens) == 0:
            print("Pilha vazia")
            return -1
        return self.itens.pop()

    def tamanho(self):
        return len(self.itens)

    def topo(self):
        if len(self.itens) == 0:
            return -1
        return self.itens[-1]

    def imprimir(self):
        print("\n")
        for item in reversed(self.itens):
            print(f" " * (abs(tamanho - item)), end="")
            print(f'##' * item)

        print("[", end=" ")
        for item in self.itens:
            print(item, end=" ")
        print("]\n")


def inicializar(pino1, discos):
    global tamanho
    print("\nTorre de Hanoi")
    print("A dificuldade dependerá do número de discos")
    print("Digite o número de discos que você deseja utilizar (de 2 a 50):")
    try:
        discos[0] = int(input())
    except ValueError:
        print("Digite um número inteiro!")
    tamanho = discos[0]
    if discos[0] not in range(2, 51):
        print("\nNúmero de discos inválido!")
        return 1
    for aux in range(discos[0], 0, -1):
        pino1.empilhar(aux)
    return 2


def terminar(pino1, pino2, pino3):
    pino1.itens.clear()
    pino2.itens.clear()
    pino3.itens.clear()


def movimentar(pino1, pino2, pino3):
    movimento = input("Digite qual destes movimentos você deseja realizar: ").upper()
    if movimento[0] not in ["A", "B", "C"] or movimento[1] not in ["A", "B", "C"]:
        print("\n MOVIMENTO INVÁLIDO! \n")
        return 2

    origem = None
    destino = None

    if movimento[0] == "A":
        origem = pino1
    elif movimento[0] == "B":
        origem = pino2
    elif movimento[0] == "C":
        origem = pino3

    if movimento[1] == "A":
        destino = pino1
    elif movimento[1] == "B":
        destino = pino2
    elif movimento[1] == "C":
        destino = pino3

    if mover(origem, destino) == 0:
        return 4
    movimentos.append(f"{movimento[0]}" + f"{movimento[1]}")
    return 5


def mover(origem, destino):
    if origem.tamanho() > 0 and (destino.tamanho() <= 0 or origem.topo() < destino.topo()):
        destino.empilhar(origem.desempilhar())
        return 1
    else:
        print("\nNão é possível realizar este movimento, você deve colocar pinos menores acima de maiores.\n")
        return 0


def mostrar_pinos(pino1, pino2, pino3):
    print("\nA: ", end="")
    pino1.imprimir()
    print("B: ", end="")
    pino2.imprimir()
    print("C: ", end="")
    pino3.imprimir()


def mostrar_possibilidades(pino1, pino2, pino3):
    print("Movimentos válidos: ", end="")
    if (pino1.topo() < pino2.topo() or pino2.tamanho() == 0) and pino1.tamanho() > 0:
        print("AB ", end="")
    if (pino1.topo() < pino3.topo() or pino3.tamanho() == 0) and pino1.tamanho() > 0:
        print("AC ", end="")
    if (pino2.topo() < pino1.topo() or pino1.tamanho() == 0) and pino2.tamanho() > 0:
        print("BA ", end="")
    if (pino2.topo() < pino3.topo() or pino3.tamanho() == 0) and pino2.tamanho() > 0:
        print("BC ", end="")
    if (pino3.topo() < pino1.topo() or pino1.tamanho() == 0) and pino3.tamanho() > 0:
        print("CA ", end="")
    if (pino3.topo() < pino2.topo() or pino2.tamanho() == 0) and pino3.tamanho() > 0:
        print("CB ", end="")
    print()

def main():
    discos = [0]
    A = Pilha()
    B = Pilha()
    C = Pilha()
    estado = inicializar(A, discos)

    while estado != 1000:
        if estado == 1:
            estado = inicializar(A, discos)
        elif estado == 2:
            mostrar_pinos(A, B, C)
            estado = 3
        elif estado == 3:
            mostrar_possibilidades(A, B, C)
            estado = 4
        elif estado == 4:
            estado = movimentar(A, B, C)
        elif estado == 5:
            if C.tamanho() == discos[0]:
                estado = 6
            else:
                estado = 2
        elif estado == 6:
            mostrar_pinos(A, B, C)
            terminar(A, B, C)
            estado = 1000

    print("Parabéns!")
    print("Jogo finalizado!")

    print(f"Movimentos realizados em ordem: {movimentos}\n")

if __name__ == "__main__":
    main()
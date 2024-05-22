class Inimigo:
    quantidade_vivos: int

    # TODO: Crie um construtor que inicializa um inimigo usando os parâmetros abaixo.
    def __init__(self, id: int, x: int, y: int, vivo: bool):
        self.id = id
        self.x = x
        self.y = y
        self.vivo = vivo

    # TODO: Método que muda a o status do inimigo de vivo para morto caso seja acertado pelo lazer na posição (X,Y). Também deve atualizar a variável quantidade_vivos.
    def foi_acertado(self, x: int, y: int) -> None:
        if self.x == x and self.y == y and self.vivo:
            self.vivo = False
            Inimigo.quantidade_vivos -= 1


if __name__ == "__main__":

    n = int(input())

    inimigos = []
    Inimigo.quantidade_vivos = n

    for id in range(n):
        x, y = map(int, input().split())
        inimigos.append(Inimigo(id, x, y, True))

    m = int(input())

    for i in range(m):
        x, y = map(int, input().split())

        for inimigo in inimigos:
            inimigo.foi_acertado(x, y)

    print(f"vivos: {Inimigo.quantidade_vivos}")
    print(f"mortos: {n - Inimigo.quantidade_vivos}")

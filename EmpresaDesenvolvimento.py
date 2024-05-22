class Projeto:
    def __init__(self, requisito_programacao, requisito_design):
        self.requisito_programacao = requisito_programacao
        self.requisito_design = requisito_design


class Empregado:
    def __init__(self, valor_por_projeto, valor_recebido):
        self.__valor_por_projeto = valor_por_projeto
        self.__valor_recebido = valor_recebido

    @property
    def valor_recebido(self):
        return self.__valor_recebido

    # Um empregado normal não é capaz de entregar nenhum projeto :(
    def capaz(self, projeto: Projeto) -> bool:
        return False

    def receber_recompensa(self) -> None:
        self.__valor_recebido += self.__valor_por_projeto


class Programador(Empregado):
    def __init__(self, valor_por_projeto: int, habilidade_programacao: int, valor_recebido: int):
        super(valor_por_projeto, valor_recebido)
        self.habilidade_programacao = habilidade_programacao
        

    def capaz(self, projeto: Projeto) -> bool:
        return self.habilidade_programacao >= projeto.requisito_programacao


class Designer(Empregado):
    def __init__(self, valor_por_projeto: int, habilidade_design: int, valor_recebido: int):
        super(valor_por_projeto, valor_recebido)
        self.habilidade_design = habilidade_design

    def capaz(self, projeto: Projeto) -> bool:
        return self.habilidade_design >= projeto.requisito_design
    


if __name__ == "__main__":

    valor, habilidade = map(int, input().split())
    programador = Programador(valor, habilidade)

    valor, habilidade = map(int, input().split())
    designer = Designer(valor, habilidade)

    n = int(input())
    for _ in range(n):
        requisito_programacao, requisito_design = map(int, input().split())
        projeto = Projeto(requisito_programacao, requisito_design)

        if programador.capaz(projeto) and designer.capaz(projeto):
            programador.valor_recebido += programador.valor_por_projeto
            designer.valor_recebido += designer.valor_por_pojeto

    print(f"Programador: R$ {programador.valor_recebido}")
    print(f"Designer: R$ {designer.valor_recebido}")

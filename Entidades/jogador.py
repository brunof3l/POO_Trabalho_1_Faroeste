from entidade import Entidade


class Jogador(Entidade):
    def __init__(self, nome: str, poder: int, defesa: int, vida_maxima: int, vida_atual: int, esquiva: int, nivel: int, exp: int, raca: str, vocacao: str, inventario: str):
        super().__init__(nome, poder, defesa, vida_maxima, vida_atual, esquiva)
        self.nivel = nivel
        self.exp = exp
        self.raca = raca
        self.vocacao = vocacao
        self.inventario = inventario

    def ganhar_exp(self, quantidade):
        self.exp += quantidade
        print(
            f"{self.nome} ganhou {quantidade} de EXP e agora está com {self.exp} de EXP!!")
        self.subir_nivel()

    def subir_nivel(self, ):
        # Para subir de nível, temos que ganhar 100 * o nível atual, ou seja 100 EXP para ir para o nível 2 e 200 de EXP para o nível 3
        exp_necessaria = self.nivel * 100

        if self.exp > exp_necessaria:
            self.exp -= exp_necessaria
            self.nivel += 1

            print(f"{self.nome} subiu para o nível {self.nivel}!!")

    def usar_item(self):
        # ?????
        pass


boneco = Jogador("Arthur Morgan", 100, 100, 200, 150, 10,
                 1, 10, "humano", "Pistoleiro", "Nada")


boneco.ganhar_exp(100)


RAÇAS_FAROESTE = {
    "Nativo":      {"poder": 3, "defesa": 1, "vida": 15, "esquiva": 6},
    "Forasteiro":  {"poder": 2, "defesa": 2, "vida": 20, "esquiva": 3},
    "Veterano":    {"poder": 1, "defesa": 4, "vida": 25, "esquiva": 1}
}

VOCAÇÕES_FAROESTE = {
    "Pistoleiro":  {"poder": 7, "defesa": 2, "vida": 10, "esquiva": 4, "item": "Revólver Colt"},
    "Xerife":      {"poder": 4, "defesa": 6, "vida": 15, "esquiva": 2, "item": "Estrela de Prata"},
    "Bandoleiro":  {"poder": 5, "defesa": 3, "vida": 12, "esquiva": 5, "item": "Shotgun"}
}

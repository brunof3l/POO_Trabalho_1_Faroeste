from entidade import Entidade


class Jogador(Entidade):
    def __init__(self, nome: str, poder: int, defesa: int, vida_maxima: int, vida_atual: int, muniçao: int, nivel: int, exp: int, raca: str, vocacao: str, inventario: dict):
        super().__init__(nome, poder, defesa, vida_maxima, vida_atual, muniçao)
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
        self.inventario = {}
        print(self.inventario)


CLASSES_FAROESTE = {
    "Indígena":      {"poder": 3, "defesa": 1, "vida": 15, "muniçao": 6},
    "Caçador de Recompensa":  {"poder": 2, "defesa": 2, "vida": 20, "muniçao": 18},
    "Veterano de Guerra":    {"poder": 1, "defesa": 4, "vida": 25, "muniçao": 18}
}

VOCAÇÕES_FAROESTE = {
    "Pistoleiro":  {"poder": 7, "defesa": 2, "vida": 10, "muniçao": 4, "item": "Revólver Colt"},
    "Rastreador":      {"poder": 4, "defesa": 6, "vida": 15, "muniçao": 2, "item": "Estrela de Prata"},
    "Caipira":  {"poder": 5, "defesa": 3, "vida": 12, "muniçao": 5, "item": "Shotgun"}
}

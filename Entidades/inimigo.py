from entidade import Entidade


class Inimigo(Entidade):
    def __init__(self, nome: str, poder: int, defesa: int, vida_maxima: int, vida_atual: int, esquiva: int, exp_recompensa: int, dificuldade: str):
        super().__init__(nome, poder, defesa, vida_maxima, vida_atual, esquiva)
        self.exp_recompensa = exp_recompensa
        self.dificuldade = dificuldade

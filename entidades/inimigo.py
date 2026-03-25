from entidades.entidade import Entidade


class Inimigo(Entidade):
    def __init__(self, nome: str, poder: int, defesa: int, vida_maxima: int, vida_atual: int, esquiva: int, exp_recompensa: int, dificuldade: str):
        super().__init__(nome, poder, defesa, vida_maxima, vida_atual, esquiva)
        self.exp_recompensa = exp_recompensa
        self.dificuldade = dificuldade


Inimigos = {
    # Nivel Facil
    "Coiote Faminto": {
        "poder": 5,
        "defesa": 2,
        "vida": 20,
        "esquiva": 10,
        "dificuldade": "Facil",
        "exp_recompensa": 50
    },
    "Lobo Pequeno": {
        "poder": 5,
        "defesa": 2,
        "vida": 20,
        "esquiva": 10,
        "dificuldade": "Facil",
        "exp_recompensa": 50
    },
    "Ladrão de Galinhas": {
        "poder": 5,
        "defesa": 2,
        "vida": 20,
        "esquiva": 10,
        "dificuldade": "Facil",
        "exp_recompensa": 50
    },
    "Bêbado do Saloon": {
        "poder": 5,
        "defesa": 2,
        "vida": 20,
        "esquiva": 10,
        "dificuldade": "Facil",
        "exp_recompensa": 50
    },
    "Abutre Faminto": {
        "poder": 5,
        "defesa": 2,
        "vida": 20,
        "esquiva": 10,
        "dificuldade": "Facil",
        "exp_recompensa": 50
    },
    # Nivel Medio
    "Ladrao de Gado": {
        "poder": 10,
        "defesa": 5,
        "vida": 40,
        "esquiva": 8,
        "dificuldade": "Médio",
        "exp_recompensa": 100
    },
    "Bandoleiro de Estrada": {
        "poder": 10,
        "defesa": 5,
        "vida": 40,
        "esquiva": 8,
        "dificuldade": "Médio",
        "exp_recompensa": 100
    },
    "Garimpeiro Ganancioso": {
        "poder": 10,
        "defesa": 5,
        "vida": 40,
        "esquiva": 8,
        "dificuldade": "Médio",
        "exp_recompensa": 100
    },
    "Capataz da Fazenda": {
        "poder": 10,
        "defesa": 5,
        "vida": 40,
        "esquiva": 8,
        "dificuldade": "Médio",
        "exp_recompensa": 100
    },
    "Desertor da Cavalaria": {
        "poder": 10,
        "defesa": 5,
        "vida": 40,
        "esquiva": 8,
        "dificuldade": "Médio",
        "exp_recompensa": 100
    },
    # Nivel Dificil
    "Pistoleiro de Aluguel": {
        "poder": 18,
        "defesa": 12,
        "vida": 85,
        "esquiva": 15,
        "dificuldade": "Difícil",
        "exp_recompensa": 200
    },
    "Assaltante de Trem": {
        "poder": 18,
        "defesa": 12,
        "vida": 85,
        "esquiva": 15,
        "dificuldade": "Difícil",
        "exp_recompensa": 200
    },
    "Xerife Corrupto": {
        "poder": 18,
        "defesa": 12,
        "vida": 85,
        "esquiva": 15,
        "dificuldade": "Difícil",
        "exp_recompensa": 200
    },
    "Urso Cinzento das Montanhas": {
        "poder": 18,
        "defesa": 12,
        "vida": 85,
        "esquiva": 15,
        "dificuldade": "Difícil",
        "exp_recompensa": 200
    },
    "Caçador de Recompensas Rival": {
        "poder": 18,
        "defesa": 12,
        "vida": 85,
        "esquiva": 15,
        "dificuldade": "Difícil",
        "exp_recompensa": 200
    },
    # Nivel Chefe
    "Xerife Renegado": {
        "poder": 30,
        "defesa": 20,
        "vida": 250,
        "esquiva": 5,
        "dificuldade": "Chefe",
        "exp_recompensa": 500
    },
    "O Coronel Sem Nome": {
        "poder": 30,
        "defesa": 20,
        "vida": 250,
        "esquiva": 5,
        "dificuldade": "Chefe",
        "exp_recompensa": 500
    },
    "O Carrasco de Black Rock": {
        "poder": 30,
        "defesa": 20,
        "vida": 250,
        "esquiva": 5,
        "dificuldade": "Chefe",
        "exp_recompensa": 500
    },
    "Billy the Kid": {
        "poder": 30,
        "defesa": 20,
        "vida": 250,
        "esquiva": 5,
        "dificuldade": "Chefe",
        "exp_recompensa": 500
    },

}

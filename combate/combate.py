import random
from sistema_dados.dados import SistemaDados


class Combate:
    def __init__(self, jogador, inimigo):

        self.jogador = jogador
        self.inimigo = inimigo
        self.dados = SistemaDados()

    def iniciar_combate(self):

        print(
            f"\n--- COMBATE INICIADO: {self.jogador.nome} vs {self.inimigo.nome} ({self.inimigo.dificuldade}) ---")

        while self.jogador.vida_atual > 0 and self.inimigo.vida_atual > 0:

            print(
                f"\n{self.jogador.nome} [HP: {self.jogador.vida_atual}/{self.jogador.vida_maxima}] [Munição: {self.jogador.muniçao}]")
            print(
                f"{self.inimigo.nome} [HP: {self.inimigo.vida_atual}/{self.inimigo.vida_maxima}]")

            print("\nO que você deseja fazer?")
            print("1 - Atacar (Gasta 1 munição)")
            print("2 - Defender (Aumenta defesa temporariamente)")
            print("3 - Usar Bandagem")
            print("4 - Fugir")

            escolha = input("Escolha uma ação: ")

            defesa_bonus_jogador = 0
            fugiu = False

            # Turno do Jogador
            if escolha == "1":
                if self.jogador.muniçao > 0:
                    self.jogador.muniçao -= 1
                    dano = self.calcular_dano(self.jogador, self.inimigo)
                    if dano > 0:
                        print(
                            f"Você acertou o {self.inimigo.nome} e causou {dano} de dano!")
                        self.inimigo.receber_dano(dano)
                    else:
                        print(f"Você errou o tiro!")
                else:
                    print("Você está sem munição! Perdeu o turno tentando atirar.")

            elif escolha == "2":
                defesa_bonus_jogador = self.jogador.defesa // 2
                print(
                    f"Você se prepara para o impacto. Defesa aumentada em {defesa_bonus_jogador} para este turno.")

            elif escolha == "3":
                self.jogador.usar_item("Bandagem")

            elif escolha == "4":
                if random.random() < 0.4:  # 40% de chance de fugir
                    print("Você conseguiu fugir com sucesso!")
                    fugiu = True
                    break
                else:
                    print("Você tentou fugir, mas o inimigo te bloqueou!")

            else:
                print("Ação inválida! Você perdeu o turno.")

            if self.inimigo.vida_atual <= 0:
                print(f"\nVitória! Você derrotou o {self.inimigo.nome}.")
                self.jogador.ganhar_exp(self.inimigo.exp_recompensa)
                break

            # Turno do Inimigo
            print(f"\nTurno do {self.inimigo.nome}...")
            dano_inimigo = self.calcular_dano(
                self.inimigo, self.jogador, defesa_bonus_jogador)

            if dano_inimigo > 0:
                print(
                    f"O {self.inimigo.nome} te atacou e causou {dano_inimigo} de dano!")
                self.jogador.receber_dano(dano_inimigo)
            else:
                print(f"O {self.inimigo.nome} errou o ataque!")

            if self.jogador.vida_atual <= 0:
                print("\nVocê foi derrotado... O deserto não perdoa os fracos.")
                return False  # Fim de jogo

        return True  # Combate terminou (vitória ou fuga)

    # Cálculo do dano
    def calcular_dano(self, atacante, defensor, bonus_defesa=0):

        # Lógica de acerto baseada em D20 vs Esquiva
        rolagem = self.dados.rolar_d20()

        if rolagem >= defensor.esquiva:

            # Dano = (Poder + D6) - (Defesa + bonus)
            dano_base = atacante.poder + self.dados.rolar_d6()
            defesa_total = defensor.defesa + bonus_defesa

            dano_final = dano_base - defesa_total

            # Retorna o maior valor entre 1 e o dano se acertar
            return max(1, dano_final)

        return 0  # Errou

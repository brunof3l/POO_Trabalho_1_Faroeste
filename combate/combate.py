import random
from sistema_dados.dados import SistemaDados


class Combate:
    def __init__(self, jogador, inimigo):

        self.jogador = jogador
        self.inimigo = inimigo
        self.dados = SistemaDados()

    def mostrar_fala_inimigo(self, situacao):
        lista = self.inimigo.falas.get(situacao, [])
        if lista:
            fala = random.choice(lista) 
            print(f"\n{self.inimigo.nome}: {fala}")

    def iniciar_combate(self):

<<<<<<< HEAD
        print(
            f"\n--- COMBATE INICIADO: {self.jogador.nome} vs {self.inimigo.nome} ({self.inimigo.dificuldade}) ---")
=======
        if self.inimigo.historia:
            print(f"\n*{self.inimigo.historia}*")

        print("="*40)
        print(f"      ---⚔️ COMBATE INICIADO ⚔️---")
        print("="*40)
        print(f"--- {self.jogador.nome} 🆚 {self.inimigo.nome} ({self.inimigo.dificuldade}) ---")

        self.mostrar_fala_inimigo("inicio")
>>>>>>> 167a6ec (alterações combate e explorar melhorado)

        while self.jogador.vida_atual > 0 and self.inimigo.vida_atual > 0:

            print(
                f"\n{self.jogador.nome} [HP: {self.jogador.vida_atual}/{self.jogador.vida_maxima}] [Munição: {self.jogador.muniçao}]")
            print(
                f"{self.inimigo.nome} [HP: {self.inimigo.vida_atual}/{self.inimigo.vida_maxima}]")

            print("\nO que você deseja fazer?")
<<<<<<< HEAD
            print("1 - Atacar (Gasta 1 munição)")
            print("2 - Defender (Aumenta defesa temporariamente)")
            print("3 - Usar Bandagem")
            print("4 - Fugir")

=======
            print("1 - Atacar ⚔️ (Gasta 1 munição)")
            print("2 - Defender 🛡️ (Aumenta defesa temporariamente)")
            print("3 - Usar Bandagem 🩹")
            print("4 - Fugir 🏃‍♂️💨")
            
>>>>>>> 167a6ec (alterações combate e explorar melhorado)
            escolha = input("Escolha uma ação: ")

            defesa_bonus_jogador = 0
            fugiu = False

            # Turno do Jogador
            if escolha == "1":
                if self.jogador.muniçao > 0:
                    self.jogador.muniçao -= 1
                    dano = self.calcular_dano(self.jogador, self.inimigo)
                    if dano > 0:
<<<<<<< HEAD
                        print(
                            f"Você acertou o {self.inimigo.nome} e causou {dano} de dano!")
=======
                        print(f"\nVocê acertou o {self.inimigo.nome} e causou {dano} de dano!")
>>>>>>> 167a6ec (alterações combate e explorar melhorado)
                        self.inimigo.receber_dano(dano)
                        self.mostrar_fala_inimigo("levou_tiro")
                    else:
                        print(f"\nVocê errou o tiro!")
                        self.mostrar_fala_inimigo("jogador_errou")
                else:
<<<<<<< HEAD
                    print("Você está sem munição! Perdeu o turno tentando atirar.")

            elif escolha == "2":
                defesa_bonus_jogador = self.jogador.defesa // 2
                print(
                    f"Você se prepara para o impacto. Defesa aumentada em {defesa_bonus_jogador} para este turno.")

=======
                    print(f"\nVocê está sem munição! Perdeu o turno tentando atirar.")
            
            elif escolha == "2":
                defesa_bonus_jogador = self.jogador.defesa // 2
                print(f"\nVocê se prepara para o impacto. Defesa aumentada em {defesa_bonus_jogador} para este turno.")
            
>>>>>>> 167a6ec (alterações combate e explorar melhorado)
            elif escolha == "3":
                self.jogador.usar_item("Bandagem")

            elif escolha == "4":
<<<<<<< HEAD
                if random.random() < 0.4:  # 40% de chance de fugir
                    print("Você conseguiu fugir com sucesso!")
                    fugiu = True
                    break
                else:
                    print("Você tentou fugir, mas o inimigo te bloqueou!")

=======
                if random.random() < 0.4: # 40% de chance de fugir
                    print(f"\nVocê conseguiu fugir com sucesso!")
                    fugiu = True
                    break
                else:
                    print(f"\nVocê tentou fugir, mas o inimigo te bloqueou!")
                    self.mostrar_fala_inimigo("inicio")
            
>>>>>>> 167a6ec (alterações combate e explorar melhorado)
            else:
                print(f"\nAção inválida! Você perdeu o turno.")

            if self.inimigo.vida_atual <= 0:
                print(f"\nVitória! Você derrotou o {self.inimigo.nome}.")
                self.mostrar_fala_inimigo("morte")
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
                self.mostrar_fala_inimigo("acertou")
            else:
                print(f"O {self.inimigo.nome} errou o ataque!")
<<<<<<< HEAD

            if self.jogador.vida_atual <= 0:
                print("\nVocê foi derrotado... O deserto não perdoa os fracos.")
                return False  # Fim de jogo
=======
                self.mostrar_fala_inimigo("errou")
            
            if self.jogador.vida_atual <= 0:
                print(f"\nVocê foi derrotado... O deserto não perdoa os fracos.")
                return False # Fim de jogo
>>>>>>> 167a6ec (alterações combate e explorar melhorado)

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

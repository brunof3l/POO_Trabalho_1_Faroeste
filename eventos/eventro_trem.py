import random
import time

from combate.combate import Combate
from entidades.inimigo import Inimigo, Inimigos


def evento_assalto_trem(jogador, dados):
    print("="*40)
    print("\ 💥🚂 ASSALTO AO TREM 🚂💥")
    print("="*40)
    print(f"\nAo longe, você vê a fumaça escura de uma locomotiva cortando o deserto.")
    time.sleep(1)
    print(f"\nO trem passa carregado de suprimentos, munição e talvez algo mais valioso.")
    time.sleep(1)
    print(f"\nUma oportunidade dessas não aparece duas vezes.")

    escolha_inicial = input(
        f"\nDeseja tentar assaltar o trem? (s/n): ").strip().lower()

    if escolha_inicial != "s":
        print("Você decide não arriscar. O trem desaparece no horizonte.")
        return True

    print("\nComo você quer agir?")
    print("1 - Subir sorrateiramente pelos fundos do trem")
    print("2 - Pular para um vagão lateral em movimento")
    print("3 - Sacar a arma e partir para o ataque de frente")

    escolha = input("Escolha uma abordagem: ").strip()

    bonus = 0
    tipo_abordagem = ""

    if escolha == "1":
        tipo_abordagem = "furtiva"
        bonus = 2
        print("\nVocê cavalga por trás da locomotiva, tentando subir sem ser notado.")
    elif escolha == "2":
        tipo_abordagem = "ousada"
        bonus = 0
        print("\nVocê acelera o cavalo e tenta saltar direto para um dos vagões.")
    elif escolha == "3":
        tipo_abordagem = "frontal"
        bonus = -2
        print("\nVocê parte pra cima sem medo, arma em punho e sangue nos olhos.")
    else:
        print("Você hesitou demais. O trem passou e a chance foi perdida.")
        return True

    print("\nVocê tenta entrar no trem...")
    rolagem_entrada = dados.rolar_d20() + bonus
    print(f"Rolagem de entrada: {rolagem_entrada} (com modificador {bonus})")

    if rolagem_entrada < 10:
        print("\nVocê falhou na aproximação!")
        if tipo_abordagem == "furtiva":
            print("Um dos guardas percebeu sua movimentação e você precisou recuar.")
        elif tipo_abordagem == "ousada":
            print("Você errou o salto e caiu na areia com violência.")
            jogador.receber_dano(8)
            print(f"{jogador.nome} perdeu 8 de HP.")
        else:
            print("Os guardas reagiram rápido e abriram fogo contra você.")
            jogador.receber_dano(12)
            print(f"{jogador.nome} perdeu 12 de HP.")
        return True

    print("\nVocê conseguiu entrar no trem!")

    print("\nAgora você precisa lidar com a segurança do vagão...")
    rolagem_confronto = dados.rolar_d20() + bonus
    print(
        f"Rolagem de confronto: {rolagem_confronto} (com modificador {bonus})")

    if rolagem_confronto < 8:
        print("\nVocê foi surpreendido pelos guardas do trem!")
        print("Um homem armado surge entre os caixotes e bloqueia seu caminho.")

        nome_guarda = "Guarda do Trem"
        stats = Inimigos[nome_guarda]

        inimigo = Inimigo(
            nome_guarda,
            stats["poder"],
            stats["defesa"],
            stats["vida"],
            stats["vida"],
            stats["esquiva"],
            stats["exp_recompensa"],
            stats["dificuldade"],
            stats.get("historia", ""),
            stats.get("falas", {})
        )

        combate = Combate(jogador, inimigo)
        if not combate.iniciar_combate():
            return False

        print("\nDepois do confronto, você revira o vagão às pressas.")
        print("Você encontrou algumas provisões antes de saltar do trem.")
        jogador.muniçao += 10
        jogador.inventario["Bandagem"] = jogador.inventario.get(
            "Bandagem", 0) + 1
        print("+10 munições")
        print("+1 Bandagem")
        return True

    elif rolagem_confronto < 15:
        print("\nVocê neutralizou os obstáculos e saqueou parte da carga.")

        recompensa = random.randint(1, 3)

        if recompensa == 1:
            print("Você encontrou um caixote de munição.")
            jogador.muniçao += 20
            print("+20 munições")

        elif recompensa == 2:
            print("Você encontrou suprimentos médicos escondidos no vagão.")
            jogador.inventario["Bandagem"] = jogador.inventario.get(
                "Bandagem", 0) + 2
            print("+2 Bandagens")

        else:
            print("Você encontrou documentos valiosos e os vendeu depois.")
            jogador.ganhar_exp(100)
            print("+100 EXP")

        return True

    else:
        print("\nVocê executou um assalto quase perfeito!")
        print("Depois de dominar o vagão principal, você encontra uma carga valiosa.")

        recompensa_grande = random.randint(1, 3)

        jogador.ganhar_exp(150)
        print("+150 EXP")

        if recompensa_grande == 1:
            jogador.muniçao += 35
            jogador.inventario["Bandagem"] = jogador.inventario.get(
                "Bandagem", 0) + 2
            print("+35 munições")
            print("+2 Bandagens")

        elif recompensa_grande == 2:
            jogador.muniçao += 25
            jogador.inventario["Bandagem"] = jogador.inventario.get(
                "Bandagem", 0) + 3
            jogador.curar(15)
            print("+25 munições")
            print("+3 Bandagens")
            print("Você ainda encontrou remédios e recuperou 15 de HP.")

        else:
            jogador.muniçao += 40
            print("+40 munições")
            print("Você encontrou uma carga rara e saiu do trem com fama ainda maior.")
            jogador.ganhar_exp(50)
            print("+50 EXP extra")

        print("Antes que reforços apareçam, você salta do trem e desaparece no deserto.")
        return True

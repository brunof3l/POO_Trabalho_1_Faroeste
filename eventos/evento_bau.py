import random

from entidades.jogador import Jogador
from sistema_dados.dados import SistemaDados


def evento_bau(jogador, dados):
    print("Você encontrou um baú antigo enterrado na areia!")
    print(
        "Você terá 3 tentativas para abri-lo. Precisa tirar 10 ou mais no D20.")

    bau_aberto = False

    for tentativa in range(1, 4):
        input(
            f"\nPressione Enter para fazer a {tentativa}ª tentativa...")
        rolagem_bau = dados.rolar_d20()
        print(
            f"Tentativa {tentativa}: você tirou {rolagem_bau} no dado.")

        if rolagem_bau >= 10:
            print("\nVocê conseguiu abrir o baú!")
            print("Dentro dele havia +12 Munição e +2 Bandagens!")
            jogador.muniçao += 12
            jogador.inventario["Bandagem"] = jogador.inventario.get(
                "Bandagem", 0) + 2
            bau_aberto = True
            break
        else:
            print("A fechadura não abriu...")

    if not bau_aberto:
        print("\nDepois de 3 tentativas, você não conseguiu abrir o baú.")
        print("Talvez precise de mais sorte na próxima vez.")
    return True

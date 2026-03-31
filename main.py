import os
import random
import time
from entidades.entidade import Entidade
from entidades.inimigo import Inimigo, Inimigos
from entidades.jogador import Jogador, CLASSES_FAROESTE, VOCAÇÕES_FAROESTE
from sistema_dados.dados import SistemaDados
from combate.combate import Combate
from eventos.eventro_trem import evento_assalto_trem as evento_trem


def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


def criar_personagem():
    limpar_tela()
    print("="*40)
    print(" 🌵 BEM VINDO A GOLDEN ROCK! 🌵 ")
    print("="*40)
    time.sleep(1)
    print("O sol do meio-dia castiga a terra rachada...")
    time.sleep(1)
    print("O vento quente traz o cheiro de pólvora e uísque barato.")
    time.sleep(1)
    print("Engraxe suas botas. Sua historia começa agora!\n")
    time.sleep(1)
    nome = input("Me diga seu nome Cowboy!\n").title()
    

    print(f"\nEscolha sua CLASSE {nome}:")
    classes = list(CLASSES_FAROESTE.keys())
    for i, c in enumerate(classes):
<<<<<<< HEAD
        print(
            f"{i+1} - {c}: Poder - {CLASSES_FAROESTE[c]["poder"]}, Defesa - {CLASSES_FAROESTE[c]["defesa"]}, Vida - {CLASSES_FAROESTE[c]["vida"]}, Munição - {CLASSES_FAROESTE[c]["muniçao"]}")
=======
        print(f"{i+1} - {c}: Poder: {CLASSES_FAROESTE[c]["poder"]}, Defesa: {CLASSES_FAROESTE[c]["defesa"]}, Vida: {CLASSES_FAROESTE[c]["vida"]}, Munição: {CLASSES_FAROESTE[c]["muniçao"]}")
>>>>>>> 167a6ec (alterações combate e explorar melhorado)
    escolha_classe = int(input("Escolha o número: ")) - 1
    classe_nome = classes[escolha_classe]
    classe_stats = CLASSES_FAROESTE[classe_nome]

    print("\nAgora escolha sua VOCAÇÃO:")
    vocacoes = list(VOCAÇÕES_FAROESTE.keys())
    for i, v in enumerate(vocacoes):
        print(f"{i+1} - {v}: Poder: {VOCAÇÕES_FAROESTE[v]["poder"]}, Defesa: {VOCAÇÕES_FAROESTE[v]["defesa"]}, Vida: {VOCAÇÕES_FAROESTE[v]["vida"]}, Munição: {VOCAÇÕES_FAROESTE[v]["muniçao"]}, Item: {VOCAÇÕES_FAROESTE[v]["item"]}")
    escolha_vocacao = int(input("Escolha o número: ")) - 1
    vocacao_nome = vocacoes[escolha_vocacao]
    vocacao_stats = VOCAÇÕES_FAROESTE[vocacao_nome]

    # Atributos Iniciais
    poder = classe_stats["poder"] + vocacao_stats["poder"]
    defesa = classe_stats["defesa"] + vocacao_stats["defesa"]
    vida_max = classe_stats["vida"] + vocacao_stats["vida"]
    municao = classe_stats["muniçao"] + vocacao_stats["muniçao"]
    esquiva = 10  # Base de esquiva

    inventario = {"Bandagem": 3}
    if "item" in vocacao_stats:
        inventario[vocacao_stats["item"]] = 1

    jogador = Jogador(
        nome=nome,
        poder=poder,
        defesa=defesa,
        vida_maxima=vida_max,
        vida_atual=vida_max,
        esquiva=esquiva,
        muniçao=municao,
        nivel=1,
        exp=0,
        raca=classe_nome,
        vocacao=vocacao_nome,
        inventario=inventario
    )

    return jogador


def escolher_inimigo_por_nivel(nivel_jogador):
    dificuldades_permitidas = ["Facil"]

    if nivel_jogador >= 3:
        dificuldades_permitidas.append("Médio")

    if nivel_jogador >= 5:
        if "Facil" in dificuldades_permitidas:
            dificuldades_permitidas.remove("Facil")
        dificuldades_permitidas.append("Difícil")

    inimigos_possiveis = [nome for nome, stats in Inimigos.items(
    ) if stats["dificuldade"] in dificuldades_permitidas]

    return random.choice(inimigos_possiveis)


def menu_principal(jogador):
    dados = SistemaDados()

    while True:
        # limpar_tela() # Removido para manter o log de combate visível
        print(
            f"\n--- {jogador.nome} | Nível: {jogador.nivel} | HP: {jogador.vida_atual}/{jogador.vida_maxima} ---")
        print("1 - Viajar 🏇🏻 (Inicia combate)")
        print("2 - Explorar 🌍 (Rola dado para eventos)")
        print("3 - Conferir Sela 🎒 (Inventário)")
        print("4 - Sair 🚪")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            # Escolher inimigo aleatório
            nome_inimigo = escolher_inimigo_por_nivel(jogador.nivel)
            stats = Inimigos[nome_inimigo]
            dados_inimigo = Inimigos[nome_inimigo]
            inimigo = Inimigo(
                nome=nome_inimigo,
                poder=stats["poder"],
                defesa=stats["defesa"],
                vida_maxima=stats["vida"],
                vida_atual=stats["vida"],
                esquiva=stats["esquiva"],
                exp_recompensa=stats["exp_recompensa"],
                dificuldade=stats["dificuldade"],
                historia=dados_inimigo.get("historia", ""),
                falas=dados_inimigo.get("falas", {})
            )

            combate = Combate(jogador, inimigo)
            vivo = combate.iniciar_combate()

            if not vivo:
                print("\nFIM DE JOGO!")
                break

        elif escolha == "2":
            rolagem = dados.rolar_d20()
            print(f"\nExplorando... Rolagem: {rolagem}")

            if rolagem >= 18:
                if not evento_trem(jogador, dados):
                    break
            
            elif rolagem >= 12:
                print("Você encontrou um baú antigo enterrado na areia!")
                print("Você terá 3 tentativas para abri-lo. Precisa tirar 10 ou mais no D20.")

                bau_aberto = False

                for tentativa in range(1, 4):
                    input(f"\nPressione Enter para fazer a {tentativa}ª tentativa...")
                    rolagem_bau = dados.rolar_d20()
                    print(f"Tentativa {tentativa}: você tirou {rolagem_bau} no dado.")

                    if rolagem_bau >= 10:
                        print("\nVocê conseguiu abrir o baú!")
                        print("Dentro dele havia +12 Munição e +2 Bandagens!")
                        jogador.muniçao += 12
                        jogador.inventario["Bandagem"] = jogador.inventario.get("Bandagem", 0) + 2
                        bau_aberto = True
                        break
                    else:
                        print("A fechadura não abriu...")

                if not bau_aberto:
                    print("\nDepois de 3 tentativas, você não conseguiu abrir o baú.")
                    print("Talvez precise de mais sorte na próxima vez.")

            
            elif rolagem >= 5:
                print("Você encontrou uma cidade pacífica e descansou um pouco.")
                jogador.curar(10)

            else:
                print("Você foi emboscado enquanto explorava!")
                nome_inimigo = escolher_inimigo_por_nivel(jogador.nivel)
                stats = Inimigos[nome_inimigo]
                inimigo = Inimigo(nome_inimigo, stats["poder"], stats["defesa"], stats["vida"],
                stats["vida"], stats["esquiva"], stats["exp_recompensa"], stats["dificuldade"], stats.get("historia", ""), stats.get("falas", {}))
                combate = Combate(jogador, inimigo)
                if not combate.iniciar_combate():
                    break

        elif escolha == "3":
            print(f"\n--- SELA DE {jogador.nome} ---")
            print(f"Classe: {jogador.raca}")
            print(f"Vocação: {jogador.vocacao}")
            print(f"Munição: {jogador.muniçao}")
            print(
                f"Nível: {jogador.nivel} (EXP: {jogador.exp}/{jogador.nivel*100})")
            print("Inventário:")
            for item, qtd in jogador.inventario.items():
                print(f" - {item}: {qtd}")

            input("\nPressione Enter para voltar...")

        elif escolha == "4":
            print("Até a próxima, parceiro!")
            break
        else:
            print("Opção inválida!")


if __name__ == "__main__":
    player = criar_personagem()
    menu_principal(player)

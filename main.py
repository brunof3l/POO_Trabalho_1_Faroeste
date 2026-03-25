import os
import random
from entidades.entidade import Entidade
from entidades.inimigo import Inimigo, Inimigos
from entidades.jogador import Jogador, CLASSES_FAROESTE, VOCAÇÕES_FAROESTE
from sistema_dados.dados import SistemaDados
from combate.combate import Combate


def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


def criar_personagem():
    limpar_tela()
    print("--- BEM-VINDO AO FAROESTE ---")
    nome = input("Digite o nome do seu pistoleiro: ")

    print("\nEscolha sua CLASSE:")
    classes = list(CLASSES_FAROESTE.keys())
    for i, c in enumerate(classes):
        print(f"{i+1} - {c}: {CLASSES_FAROESTE[c]}")
    escolha_classe = int(input("Escolha o número: ")) - 1
    classe_nome = classes[escolha_classe]
    classe_stats = CLASSES_FAROESTE[classe_nome]

    print("\nEscolha sua VOCAÇÃO:")
    vocacoes = list(VOCAÇÕES_FAROESTE.keys())
    for i, v in enumerate(vocacoes):
        print(f"{i+1} - {v}: {VOCAÇÕES_FAROESTE[v]}")
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
        
    inimigos_possiveis = [nome for nome, stats in Inimigos.items() if stats["dificuldade"] in dificuldades_permitidas]
    
    return random.choice(inimigos_possiveis)


def menu_principal(jogador):
    dados = SistemaDados()

    while True:
        # limpar_tela() # Removido para manter o log de combate visível
        print(
            f"\n--- {jogador.nome} | Nível: {jogador.nivel} | HP: {jogador.vida_atual}/{jogador.vida_maxima} ---")
        print("1 - Viajar (Inicia combate)")
        print("2 - Explorar (Rola dado para eventos)")
        print("3 - Conferir Sela (Inventário)")
        print("4 - Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            # Escolher inimigo aleatório
            nome_inimigo = escolher_inimigo_por_nivel(jogador.nivel)
            stats = Inimigos[nome_inimigo]
            inimigo = Inimigo(
                nome=nome_inimigo,
                poder=stats["poder"],
                defesa=stats["defesa"],
                vida_maxima=stats["vida"],
                vida_atual=stats["vida"],
                esquiva=stats["esquiva"],
                exp_recompensa=stats["exp_recompensa"],
                dificuldade=stats["dificuldade"]
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
                print("Você encontrou um TESOURO escondido! +50 Munição e +2 Bandagens")
                jogador.muniçao += 50
                jogador.inventario["Bandagem"] = jogador.inventario.get(
                    "Bandagem", 0) + 2
            elif rolagem >= 12:
                print("Você assaltou um trem com sucesso! +100 EXP")
                jogador.ganhar_exp(100)
            elif rolagem >= 5:
                print("Você encontrou uma cidade pacífica e descansou um pouco.")
                jogador.curar(10)
            else:
                print("Você foi emboscado enquanto explorava!")
                nome_inimigo = escolher_inimigo_por_nivel(jogador.nivel)
                stats = Inimigos[nome_inimigo]
                inimigo = Inimigo(nome_inimigo, stats["poder"], stats["defesa"], stats["vida"],
                                  stats["vida"], stats["esquiva"], stats["exp_recompensa"], stats["dificuldade"])
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

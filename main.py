import random

#variaveis

#cerebro_computador
pedra = 1
papel = 2
tesoura = 3

#chave
saida = False

#entrada :)
#processamento
#saida

#ligado ou desligado
while saida == False:
    escolha_pc = ""

    #ensinar
    print("papel pedra ou tesoura")

    #player escolhendo
    jogador = input("Qual sua escolha: ")#<------

    #computador escolheu
    escolha = random.randint(1,3)#<------
    print("o num é 3 ", escolha)

    #processamento

    #transforma a escolha do pc
    if escolha == 1:
        escolha_pc = "pedra"

    elif escolha == 2:
        escolha_pc = "papel"

    else:
        escolha_pc = "tesoura"

    #resultado
    if jogador == "pedra":
        if escolha_pc == "papel":
            print("o pc escolheu papel, Voce perdeu!")
        elif escolha_pc == "tesoura":
            print("voce ganhou, o pc escolheu tesoura")
        else:
            print("empate")

    elif jogador == "papel":
        if escolha_pc == "papel":
            print("empate")
        elif escolha_pc == "tesoura":
            print("o pc escolheu tesoura, Voce perdeu!")
        else:
            print("voce ganhou, o pc escolheu pedra")

    elif jogador == "tesoura":
        if escolha_pc == "papel":
            print("voce ganhou, o pc escolheu papel")

        elif escolha_pc == "tesoura":
            print("empate")

        else:
            print("o pc escolheu pedra, Voce perdeu!")

    elif jogador == "sair":
        saida == True

    else:
        print("entrada errada")
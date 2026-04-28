import random

#lista de opções
opcoes = ["pedra", "papel", "tesoura"]

while True:
    print("Pedra, papel ou tesoura (ou 'sair')")
    #escolha do jogador
    jogador = input("Sua escolha: ").lower()

    #ver a saida
    if jogador == "sair":
        break
    
    #verifica se recebeu as opções corretas
    if jogador not in opcoes:
        print("Entrada inválida\n")
        continue
    
    #escolha do pc
    escolha_pc = random.choice(opcoes)

    print(f"PC escolheu: {escolha_pc}")

    #ver quem ganhou ou se foi empate
    if jogador == escolha_pc:
        print("Empate\n")
    elif (
        (jogador == "pedra" and escolha_pc == "tesoura") or
        (jogador == "papel" and escolha_pc == "pedra") or
        (jogador == "tesoura" and escolha_pc == "papel")
    ):
        print("Você ganhou!\n")
    else:
        print("Você perdeu!\n")
import random

opcoes = ["pedra", "papel", "tesoura"]

while True:
    print("Pedra, papel ou tesoura (ou 'sair')")
    
    jogador = input("Sua escolha: ").lower()

    if jogador == "sair":
        break

    if jogador not in opcoes:
        print("Entrada inválida\n")
        continue

    escolha_pc = random.choice(opcoes)

    print(f"PC escolheu: {escolha_pc}")

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
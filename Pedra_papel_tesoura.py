import random

def jogar():
    while True:
        jogador_escolha = input("Escolha Pedra, Papel ou Tesoura: ").lower()
        if jogador_escolha not in ["pedra", "papel", "tesoura"]:
            print("Escolha inválida. Por favor, escolha Pedra, Papel ou Tesoura.")
            continue

        opcoes = ["pedra", "papel", "tesoura"]
        computador_escolha = random.choice(opcoes)

        print(f"Você escolheu {jogador_escolha}.")
        print(f"O computador escolheu {computador_escolha}.")

        if jogador_escolha == computador_escolha:
            print("Empate!")
        elif jogador_escolha == "pedra" and computador_escolha == "tesoura" or \
             jogador_escolha == "papel" and computador_escolha == "pedra" or \
             jogador_escolha == "tesoura" and computador_escolha == "papel":
            print("Você ganhou!")
        else:
            print("Você perdeu!")

        jogar_novamente = input("Deseja jogar novamente? (s/n): ")
        if jogar_novamente.lower() != "s":
            break

if __name__ == "__main__":
    jogar()

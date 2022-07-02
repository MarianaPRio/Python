import random

def jogo_adivinhacao():

    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    numero_secreto = random.randrange(1,101)
    pontuacao = 1000

    print("Qual nivel de dificuldade?\n")
    print("(1) Facil (2) Medio (3) Difil")

    nivel = int(input("Defina o nivel: "))

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5


    for rodada in range(1, total_de_tentativas+1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))

        chute_str = input("Digite o seu numero entre 1 e 100: ")
        print("Voce digitou ", chute_str)
        chute = int(chute_str)

        if(chute < 1 or chute > 100):
            print("Voce deve digitar um numero entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if(acertou):
            print("Voce acertou!")
            print("Sua pontuacao foi de: {}".format(pontuacao))
            break
        else:
            if(maior):
                print("Seu chute foi maior que o numero secreto!")

            elif(menor):
                print("Seu chute foi menor que o numero secreto!")     
            pontos_perdidos = abs(numero_secreto - chute)
            pontuacao = pontuacao - pontos_perdidos

    print("\n")
    print("O numero secreto era: {}".format(numero_secreto))
    print("Fim de jogo.")

if(__name__ == "__main__"):
    jogo_adivinhacao()
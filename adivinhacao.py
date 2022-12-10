import random
print("********************************")
print("Bem vindo ao jogo de Adivinhacao")
print("********************************")
numero_random = random.random() * 100
numero_secreto = round(numero_random)
total_tentativas = 3

for rodada in range(1, total_tentativas+1):
    print("Tentativa {} de {}".format(rodada, total_tentativas))

    chute_str = input("Digite um numero entre 1 e 100: ")
    print("Voce digitou ", chute_str)
    chute = int(chute_str)

    if(chute < 1 or chute > 100):
        print("Voce deve difitar um numero entre 1 e 100!")
        continue

    acertou = numero_secreto == chute
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if(acertou):
            print("Voce acertou!")
            break
    else:
        if(maior):
            print("Voce errou: O seu chute foi maior que o numero secreto.")
        elif(menor):
            print("Voce errou: O seu chute foi menor que o numero secreto.")

print("Fim de jogo")
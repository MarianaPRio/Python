import adivinhacao
import forca

def jogo_jogos():
    print("*********************************")
    print("********Escolha seu jogo!********")
    print("*********************************")

    print("(1) Adivinhacao (2) Forca")

    jogo = int(input("Qual o jogo? "))

    if(jogo == 1):
        print("Jogando Adivinhacao")
        adivinhacao.jogo_adivinhacao()
    elif(jogo == 2):
        print("Jogando Forca")
        forca.jogo_forca()


if(__name__ == "__main__"):
    jogo_jogos()
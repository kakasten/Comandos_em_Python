
import random

#Menu

def usar():

    imprimeMensagemAbertura()
    palavraSecreta = carregaPlavraSecreta()
   
    letrasAcertadas = IncializaLetrasAcertadas(palavraSecreta)
    print(letrasAcertadas)

    enforcou = False
    acertou = False
    tentativas = 0

    

    while(not enforcou and not acertou):

        chute = pede_chute()
        
        if(chute in palavraSecreta):
            marca_chute_correto(chute,palavraSecreta,letrasAcertadas)
        
        else:
            tentativas += 1
            desenha_forca(tentativas)
        
        enforcou = tentativas == 7
        acertou = "_" not in letrasAcertadas
        print(letrasAcertadas)

    if(acertou):
        print("Parabéns, você ganhou!")
        print("       ___________      ")
        print("      '._==_==_=_.'     ")
        print("      .-\\:      /-.    ")
        print("     | (|:.     |) |    ")
        print("      '-|:.     |-'     ")
        print("        \\::.    /      ")
        print("         '::. .'        ")
        print("           ) (          ")
        print("         _.' '._        ")
        print("        '-------'       ")
    else:

        print("Puxa, você foi enforcado!")
        print("A palavra era {}".format(palavraSecreta))
        print("    _______________         ")
        print("   /               \       ")
        print("  /                 \      ")
        print("//                   \/\  ")
        print("\|   XXXX     XXXX   | /   ")
        print(" |   XXXX     XXXX   |/     ")
        print(" |   XXX       XXX   |      ")
        print(" |                   |      ")
        print(" \__      XXX      __/     ")
        print("   |\     XXX     /|       ")
        print("   | |           | |        ")
        print("   | I I I I I I I |        ")
        print("   |  I I I I I I  |        ")
        print("   \_             _/       ")
        print("     \_         _/         ")
        print("       \_______/           ")



    
def imprimeMensagemAbertura():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

def carregaPlavraSecreta():
    arquivo = open("palavras.txt","r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)        
        
    arquivo.close()

    numero = random.randrange(0,len(palavras))
    palavraSecreta = palavras[numero].upper()
    return palavraSecreta

def IncializaLetrasAcertadas(palavraSecreta):
    return ["_" for letra in palavraSecreta]

def pede_chute():
        chute = input ("Qual letra? ")
        chute = chute.strip().upper()
        return chute

def marca_chute_correto(chute,palavraSecreta,letrasAcertadas):
    
    index = 0 
    for letra in palavraSecreta: 

        if(chute == letra):
            letrasAcertadas[index] = letra
    index += 1 

def desenha_forca(tentativas):
    print("  _______     ")
    print(" |/      |    ")

    if(tentativas == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(tentativas == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(tentativas == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(tentativas == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(tentativas == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(tentativas == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (tentativas == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

if(__name__ == "__main__"):
    usar()
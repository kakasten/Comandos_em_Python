import Forca
import Adivinhação
import Calculadora

print("*********************************")
print("*******Escolha o seu jogo!*******")
print("*********************************")

print("1. Forca")
print("2. Adivinhação")
print("3. Calculadora")

jogo = int (input ("Qual jogo?"))

if(jogo == 1 ):
    print ("Jogando forca ")
    Forca.usar()
elif(jogo == 2):
    print ("Jogando adivinhação ")
    Adivinhação.usar()
else:
    print("Usando Calculadora ")
    Calculadora.usar()

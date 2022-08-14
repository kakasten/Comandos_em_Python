
def usar():

    #Desafio prof Ana

    print ("Bem vindo a calculadora")

    iniciar = 1

    while (iniciar >= 1):

        print ("qual operação deseja fazer?")
        print ("1. Somar")
        print ("2. Subtrair")
        print ("3. Mutiplicar")
        print ("4. Dividir")

        operacao = int (input ("Digite: "))

        x = float (input ("Digite o primeiro valor: "))
        y = float (input ("Digite o segundo valor: "))

        somar = float ((x + y))
        subtrair = float ((x - y))
        mutiplicar = float ((x * y))
        dividir = float ((x / y))

        if (operacao == 1):
            valor = somar
        elif(operacao == 2):
            valor = subtrair
        elif(operacao == 3):
            valor = mutiplicar
        elif(operacao ==4):
            valor = dividir
        
        print(valor)

        print("Você quer continuar?")
        print("1. Sim!")
        print("2. Não!")

        continuar = int (input ("Digite:"))

        if (continuar  == 1):

            iniciar = 1

        else:

            iniciar = 0
            
if(__name__ == "__main__"):
    usar()

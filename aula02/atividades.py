#peso1 = float(input("Diga seu peso primeira pessoa: "))
#peso2 = float(input("Diga seu peso segunda pessoa: "))

#if peso1 > peso2 :
    #print("Primeira pessoa mais pesada")
#elif peso2 > peso1 :
    #print("Segunda pessoa mais pesada")
#else:
    #print("Mesmo peso")


#num = int(input("Digite um numero: "))

#if num % 2 == 0:
    #quadrado = num * num
    #print(quadrado)
#else:
    #cubo = num * num * num
    #print(cubo)


#num1 = float(input("Escreva o primeiro número: "))
#num2 = float(input("Escreva o segundo número: "))
#num3 = float(input("Escreva o terceiro número: "))

#if num1 > num2 and num1 > num3:
    #maior = num1
    #if num2 > num3:
        #meio = num2
        #menor = num3
    #else:
        #meio = num3
        #menor = num2

#elif num2 > num1 and num2 > num3:
    #maior = num2
    #if num1 > num3:
        #meio = num1
        #menor = num3
    #else:
        #meio = num3
        #menor = num1

#else:
    #maior = num3
    #if num1 > num2:
        #meio = num1
        #menor = num2
    #else:
        #meio = num2
        #menor = num1

#print(f"Pessoa 1 {maior}")
#print(f"Pessoa 2 {meio}")
#print(f"Pessoa 3 {menor}")


num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))

entrada = int(input("O que deseja fazer com esses valores? \n 1 - Média \n 2 - Quadrado \n 3 - Cubo \n"))

if entrada == 1:
    media = (num1 * 2) + (num2 * 3) / 2 + 3
    print(media)

elif entrada == 2:
    soma = num1 + num2
    quadrado = soma * soma
    print(quadrado)

elif entrada == 3:
    if num1 < num2:
        menor = num1
    else:
        menor = num2

    cubo = menor * menor * menor

    print(cubo)

else:
    print("Dado inválido")


    


 








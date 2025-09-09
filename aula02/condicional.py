#entrada = input ('Você quer entrar ou sair?')

#if entrada == 'entrar' :
    #print('Você entrou no sistema')
#elif entrada == 'sair' :
    #print('Você saiu do sistema')
#else :
    #print("Você digitou um comando inválido")


#nota1 = float(input('Informe a nota do primeiro bimestre'))
#nota2 = float(input('Informe a nota do segundo bimestre'))

#media = (nota1 + nota2) / 2

#if media > 6 :
    #print('Aprovado')
#else :
    #print('Reprovado')


#print("## Programa de Empréstimos ##\nResponda (0 - Não e 1 - Sim)")

#negativado = int(input("Possui nome negativado? "))

#if negativado == 1:
    #print("Não pode realizar empréstimo")
#else:
    #carteiraAssinada = int(input("Possui carteira assinada? "))
    
    #if carteiraAssinada == 0:
        #print("Não pode realizar empréstimo")
    #else:
        #possuiCasaPropria = int(input("Possui casa própria? "))
        
        #if possuiCasaPropria == 0:
            #print("Não pode realizar empréstimo")
        #else:
            #print("Conceder empréstimo")


numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
numero3 = int(input("Digite o terceiro número: "))

if numero1 == numero2 or numero2 == numero3 or numero1 == numero3:
    exit() #encerra o programa
if numero1 > numero2 and numero1 > numero3:
    print("Primeiro número é maior")
if numero2 > numero1 and numero2 > numero3:
    print("Segundo número é maior")
if numero3 > numero1 or numero3 > numero2:
    print("Terceiro número é maior")
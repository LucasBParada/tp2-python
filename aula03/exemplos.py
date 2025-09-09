#opcao = input("Digite uma letra: ").lower()

#match opcao:
    #case 'a'|'e'|'i'|'o'|'u':
        #print("Isso é uma vogal! ")

    #case _:
        #print("Isso é uma consoante! ")

#registro = int(input("Digite seu índice de poluição: "))
#match registro:
    #case 0|1|2:
        #print("Seu índice é aceitável")
    #case 3|4|5:
        #print("Suspenda as atividades do Grupo 1")
    #case 6|7:
        #print("Suspenda as atividades do Grupo 1 e 2")
    #case _:
        #print("Suspenda as atividades de todos os grupos")

opcoes = input("Digite o que deseja calcular: \n 1 - Tensão \n 2 - Resistência \n 3 - Corrente \n").lower()

match opcoes:
    case 'tensao':
        resistencia = float(input("Digite a resistencia: "))
        corrente = float(input("Digite a corrente: "))
        tensao = resistencia * corrente
        print(tensao)
    case 'resistencia':
        tensao = float(input("Digite a tensao: "))
        corrente = float(input("Digite a corrente:"))
        resistencia = tensao * corrente
        print(resistencia)
    case 'corrente':
        tensao = float(input("Digite a tensao: "))
        resistencia = float(input("Digite a resistencia: "))
        corrente = resistencia * tensao
        print(corrente)
    case _:
        print("Comando errado")





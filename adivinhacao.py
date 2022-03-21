print("\n*********************************")
print("Bem vindo ao jogo de adivinhação!")
print("*********************************")

numero_secreto = 22
tentativas = 5
dicas_recebidas = 0

jogar = 1
while jogar:
    print("\n=======MENU=======")
    print("1-Chutar um número")
    print("2-Receber uma dica")
    print("==================")

    opcao = int(input("Sua escolha: "))

    # Chute
    if(opcao == 1):
        chute = int(input("Seu chute: "))

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print("\nParabéns, você acertou!")
            print("O número secreto é:", numero_secreto)
            break
        elif (maior):
            print("\nErrou!\nTente um número menor que", chute)
        else:
            print("\nErrou!\nTente um número maior que", chute)
        tentativas -= 1
        print("Você tem mais", tentativas, "tentativas")

        if (tentativas == 0):
            print("\nTentativas esgotadas")
            break
    # Dicas
    elif(opcao == 2):
        if(dicas_recebidas == 0):
            # Dica 1
            print("É um número entre 1 e 30")
            dicas_recebidas += 1
        elif(dicas_recebidas == 1):
            # Dica 2
            if(numero_secreto % 2 == 0):
                print("É um número par")
            else:
                print("É um número ímpar")
            dicas_recebidas += 1
        elif (dicas_recebidas == 2):
            # Dica 3
            if(numero_secreto <= 15 and numero_secreto > 0):
                print("É um número de 1 a 15")
            elif(numero_secreto > 15 and numero_secreto <= 30):
                print("É um número de 16 a 30")
            dicas_recebidas += 1
        else:
            print("Número de dicas esgotado!")
    else:
        print("Opção inválida!")


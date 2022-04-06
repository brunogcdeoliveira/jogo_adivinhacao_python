import forca
import adivinhacao

print("*"*33)
print("******** Escolha um jogo ********")
print("*"*33)

print("\n(1) Forca - (2) Adivinhação")
jogo_selecionado = int(input("Sua escolha: "))
# print(jogo_selecionado)

if(jogo_selecionado == 1):
    print("você selecionou o jogo da forca")
    forca.jogo()
elif(jogo_selecionado == 2):
    print("você selecionou o jogo de adivinhação")
    adivinhacao.jogo()
else:
    print("Selecione um jogo válido")
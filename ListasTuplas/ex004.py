# Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.

palavras = str(input(''))
consolantes = []
vogais = []
for i in range(1):
    while True:
        try:
            num = input(f"Digite o número {i+1}: ")
            letras.append(num)
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número real.")

print("Os números digitados foram:")
for num in vetor:
    print(num)
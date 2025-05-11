# Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.

vetor = []
print("Digite 5 números inteiros:")
for i in range(5):
    while True:
        try:
            num = int(input(f"Digite o número {i+1}: "))
            vetor.append(num)
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

print("Os números digitados foram:")
for num in vetor:
    print(num)

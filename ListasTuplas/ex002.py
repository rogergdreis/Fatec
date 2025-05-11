# Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.

vetor = []
print("Digite 10 números reais:")
for i in range(10):
    while True:
        try:
            num = float(input(f"Digite o número {i+1}: "))
            vetor.append(num)
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número real.")

print("Os números digitados foram:")
for num in reversed(vetor):
    print(num)

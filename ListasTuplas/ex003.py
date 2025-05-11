# Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

notas = []
print("Digite as 4 notas:")
for i in range(4):
    while True:
        try:
            nota = float(input(f"Digite a nota número {i+1}: "))
            notas.append(nota)
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite uma nota válida.")

print("As notas digitadas foram:")
for nota in notas:
    print(nota)

print('A média: {:.1f}'.format(sum(notas) / len(notas)))
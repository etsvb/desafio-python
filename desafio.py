print("ESCOLHA A CERVEJA PELO NÚMERO")
print("1 - ANTARCTICA R$6.00")
print("2 - SKOL R$6.50")
print("3 - BRAHMA R$8.20")
print("4 - SOL R$8.25")
print("5 - NORTENHA R$16.80")
print("6 - PROIBIDA R$4.80")
print("7 - DEVASSA R$5.90")
print("8 - HEINEKEN R$9.00")

cerveja = int(input("Digite o número da cerveja: "))
q = float(input("Quantas? "))

if cerveja == 1:
    nome = "Antarctica"
    valor_cerveja = 6 * q
elif cerveja == 2:
    nome = "Skol"
    valor_cerveja = 6.5 * q
elif cerveja == 3:
    nome = "Brahma"
    valor_cerveja = 8.2 * q
elif cerveja == 4:
    nome = "Sol"
    valor_cerveja = 8.25 * q
elif cerveja == 5:
    nome = "Nortenha"
    valor_cerveja = 16.8 * q
elif cerveja == 6:
    nome = "Proibida"
    valor_cerveja = 4.8 * q
elif cerveja == 7:
    nome = "Devassa"
    valor_cerveja = 5.9 * q
elif cerveja == 8:
    nome = "Heineken"
    valor_cerveja = 9 * q
else:
    print("Valor inválido!")
    exit()

print(f"{nome} custa R${valor_cerveja:.2f} por {q} cerveja(s).")
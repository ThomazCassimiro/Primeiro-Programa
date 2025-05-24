nome = input("Digite seu nome: ")

print(f'Olá {nome}, seja bem-vindo(a)')

idade = int(input("Digite sua idade: "))

print(f"Você tem {idade} anos")

if idade < 18:
    print(f"{nome}, você é menor de idade, pois vc tem {idade} anos")
else:
    print(f"{nome}, você é a maior de idade.")

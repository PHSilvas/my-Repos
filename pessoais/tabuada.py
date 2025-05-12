def tabuada(numero):
    print(f"\nTabuada do {numero}:")
    for ct in range(1, 11):
        resultado = numero * ct
        print(f"{numero} x {ct} = {resultado}")

try:
    a = int(input("Digite um número inteiro: "))
    tabuada(a)
except ValueError:
    print("Por favor, digite um número válido.")

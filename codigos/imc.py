def calcularIMC (peso, altura):
   return round(peso / (altura * altura), 1)

peso = int(input("informe seu peso"))
altura = float(input("informe sua altura"))

print(f"o seu imc é {calcularIMC(peso=peso, altura=altura)}")

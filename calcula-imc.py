# Cálculo de IMC
peso = float(input("Digite seu peso (em kg): "))
alt = float(input("Digite sua altura (em metros): "))

imc = peso / (alt * alt)

print("Seu IMC é: ", imc)

if imc <= 18.5:
    print("Magreza")
elif imc > 18.5 and imc <= 24.9:
    print("Saudável (normal)")
elif imc > 24.9 and imc <= 29.9:
    print("Sobrepeso")
elif imc > 29.9 and imc <= 34.9:
    print("Obesidade Grau I")
elif imc > 34.9 and imc <= 39.9:
    print("Obesidade Grau II")
elif imc > 39.9:
    print("Obesidade Mórbida")
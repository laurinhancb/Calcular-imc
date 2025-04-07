# Cálculo de IMC com validação e dicas
while True:
    try:
        peso = float(input("Digite seu peso (em kg): "))
        altura = float(input("Digite sua altura (em metros): "))
        
        if peso <= 0 or altura <= 0:
            print("Valores inválidos! Peso e altura devem ser positivos.\n")
            continue
            
        imc = peso / (altura ** 2)
        break
        
    except ValueError:
        print("Entrada inválida! Use números (ex: 68.5 ou 1,75).\n")

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
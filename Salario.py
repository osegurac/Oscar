Empleador = 0.30
Trabajador = 0.10
while True:
    try:
        Salario = int(input("Digite el Salario "))
        break
    except:
        print("Digite un numero")
Total = int((Salario*Empleador)+(Salario*Trabajador))
print("El total de las cargas sociales es", Total)
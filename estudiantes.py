lista=[]
while True:
    Seleccionar=input()
    if Seleccionar=="1":
        Estudiante=input("Nombre ")
        lista.append(Estudiante)
    elif Seleccionar=="2":
        print(lista)
        Opcion=int(input("Ingrese opcion "))
        lista.pop=(Opcion)
    elif  Seleccionar=="3":
        break
print(lista)
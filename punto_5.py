print("Punto 5")
arreglo = [1,2,1,3,3,1,2,1,5,1]
mostrar = ""
for i in range (5):
    for l in range(len(arreglo)):
        if (i+1)==arreglo[l]:
            mostrar+="*"
    print(f"{i+1}/{mostrar}")
    mostrar = ""
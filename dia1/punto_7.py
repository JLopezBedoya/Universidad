print("punto 7")
arreglo = [1,3,4,2,7,0]
for i in range(len(arreglo)):
    for l in range (len(arreglo)):
        if (arreglo[i]+arreglo[l]) == 10:
            print(f"{arreglo[i]}+{arreglo[l]} = 10")

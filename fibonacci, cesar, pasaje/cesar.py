abc = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 
       'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 
       'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 
       'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
palabra = input("Ingrese una palabra: ")
c = int(input("Corrimiento: "))
codigo = ""
for i in range (len(palabra)):
    for k in range(len(abc)):
        if palabra[i]==abc[k]:
            codigo+= abc[k-c]
    if palabra[i] not in abc:
        codigo+=palabra[i]
print(codigo)

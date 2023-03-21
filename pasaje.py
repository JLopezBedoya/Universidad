print("Compañia de turimos random")
def vuelo(t, c, e, s):
    precio = 5000000
    aumento = 0
    descuento = 0
    if c == 1 and t==1:
        aumento+= precio*0.2
    elif c == 2 and t==1:
        aumento+= precio*0.3
    if e<18:
        descuento+= precio*0.5
    if e>60:
        aumento+=100000
    if c==2 and e>=18 and t==2:
        descuento+= precio*0.1
    precio-=descuento
    precio+=aumento
    return precio
while(True):
    try:
        tmp = int(input("\nTemporada del vuelo (1.Alta/2.Baja): "))
        comp = int(input("Compañia (1.Volar/2.Alas): "))
        edad = int(input("Digite su edad: "))
        est = int(input("Es usted un estudiante? (1.Si/2.No): "))
        if (tmp>2 or comp>2 or est>2):
            print("\nLas respuestas exceptuando edad deben ir del 1 al 2")
            input("presione enter para reiniciar el formulario")
            continue
        else:
            print(vuelo(tmp, comp, edad, est))
            input()
    except:
        print("\nTodos Los valores del formularios son numericos")
        input("presione enter para reiniciar el formulario")
        continue
    
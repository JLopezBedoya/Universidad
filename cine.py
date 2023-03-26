print("CINE RANDOM")
while(True):
    tipo = input("Salas: \nDinamix - 18800 \n3D - 15500 \n2D - 11500 \nCual es su tipo de sala?: ").lower()
    if tipo != "dinamix" and tipo != "2d" and tipo != "3d":
        print("Por favor elija una de las opciones dadas (dinamix, 2d, 3d)")
        continue
    cantidad = int(input("Cuantas entradas desea comprar?: "))
    card = input("Pagara con la tarjeta del cine?(S/N): ").lower()
    if card=="s":
        tarjeta = True
    elif card=="n":
        tarjeta = False
    else:
        print("Por favor lija las opciones dadas S(si) o N(no)")
        continue
    
    res = input("Tiene reserva?(S/N): ").lower()
    if res=="s":
        reserva = True
    elif res=="n":
        reserva = False
    else:
        print("Por favor lija las opciones dadas S(si) o N(no)")
        continue
    
    hora = input("Es hora pico?(S/N): ").lower()
    if hora=="s":
        pico = True
    elif hora=="n":
        pico = False
    else:
        print("Por favor lija las opciones dadas S(si) o N(no)")
        continue
    info_cine = {
        "cantidad_boletas": cantidad,
        "tipo_sala": tipo,
        "hora_pico": pico,
        "pago_tarjeta_cinema": tarjeta,
        "reserva": reserva
    }
    break
def calcular_costo_boletas(info_cine: dict):
    descuento = 0
    aumento = 0
    varios = 0
    if info_cine["tipo_sala"] == "2d":
        valor = 11300
    elif info_cine["tipo_sala"] == "3d":
        valor = 15500
    elif info_cine["tipo_sala"] == "dinamix":
        valor = 18800
    
    if info_cine["hora_pico"] and (info_cine["tipo_sala"]== "2d" or info_cine["tipo_sala"]== "3d"):
        aumento+= valor*0.25
    elif info_cine["hora_pico"] and info_cine["tipo_sala"] == "dinamix":
        aumento+= valor*0.5
    else:
        if info_cine["cantidad_boletas"]>=3:
            varios-=info_cine["cantidad_boletas"]*500
        descuento += valor*0.1
    
    if info_cine["pago_tarjeta_cinema"]:
        descuento+=valor*0.05
    
    if info_cine["reserva"]:
        varios+=info_cine["cantidad_boletas"]*2000
    total = valor+aumento
    total-=descuento
    total*=info_cine["cantidad_boletas"]
    total+=varios
    return total
    
print(calcular_costo_boletas(info_cine))

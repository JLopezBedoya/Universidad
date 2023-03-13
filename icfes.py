import pandas
from os import system
archivo = pandas.read_csv("icfes.csv")
def porcentaje_estratos(datos):
    final = pandas.DataFrame(columns=["hombres", "mujeres"])
    estratos = {
        1: [0,0],
        2: [0,0],
        3: [0,0],
        4: [0,0]
    }
    for i in range(4):
        mujeres = len(datos[(datos["genero"]=="F")&(datos["estrato"]==1+i)])
        estratos[1+i][0] = mujeres
    for f in range(4):
        hombres = len(datos[(datos["genero"]=="M")&(datos["estrato"]==1+f)])
        estratos[1+f][1] = hombres

    for k in range(4):
        h = estratos[1+k][1]
        m = estratos[1+k][0]
        final = final.append({"hombres":h, "mujeres": m}, ignore_index=True)
    return final
        
def promedio_departamentos(datos):
    final = pandas.DataFrame(columns=["departamento", "promedio"])
    
    departamento = ['huila', 'casanare', 'meta', 'narino', 'quindio', 
                    'risaralda', 'cundinamarca', 'boyaca', 'santander', 'putumayo',
                    'bogota', 'barranquilla', 'caldas', 'tolima', 'amazonas']
    
    for i in range (len(departamento)):
        dep = datos[(datos["departamento"]==departamento[i])]
        prom = (sum(dep["puntaje"]))/(len(dep))
        final = final.append({"departamento":{departamento[i]:prom}}, ignore_index=True)
    top = (final.sort_values("promedio", ascending = False)).head(10)
    return top

estrato = porcentaje_estratos(archivo).to_dict()
promedio = promedio_departamentos(archivo).to_dict()
system("clear")
usuario = int(input("estrato a consultar: "))
muestra = {"Estrato": ("F: ",estrato["mujeres"][usuario-1], "H: ", estrato["hombres"][usuario-1]), 
           "puntuacion global": promedio}
print(muestra)

    
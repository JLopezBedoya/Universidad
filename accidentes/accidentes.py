import pandas
archivo = pandas.read_csv("accidentes.csv")
data = archivo[(archivo["CALLE_NUMERO"]==30)]
def calle30(archivo):
    tipo = {"Con Muertos":0, 
            "Con Heridos":0,
            "Con Solo daños":0
            }
    tipo["Con Muertos"]= len(archivo[(archivo["GRAVEDAD_ACCIDENTE"]=="Con muertos")])
    tipo["Con Heridos"]= len(archivo[(archivo["GRAVEDAD_ACCIDENTE"]=="Con heridos")])
    tipo["Con Solo daños"]= len(archivo[(archivo["GRAVEDAD_ACCIDENTE"]=="Solo daños")])
    fecha = archivo["FECHA_ACCIDENTE"].tail(1)
    fecha = fecha.iloc[[0][0]]
    clase = archivo["CLASE_ACCIDENTE"].value_counts()
    clase = list(((clase.head(1)).to_dict()).items())
    return {"Clase_Mas_Accidente": clase,
            "Accidentes_Gravedad": tipo,
            "Cantidad_Max_Heridos": (tipo["Con Heridos"], fecha)}
print(calle30(data))
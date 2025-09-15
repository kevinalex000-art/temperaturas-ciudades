# --------------------------------------------
# Función para calcular el promedio de temperaturas
# Autor: Kevin Alexander Ramos Cabrera
# --------------------------------------------

def calcular_promedio_temperaturas(datos):
    """
    Calcula el promedio de temperaturas por ciudad.
    
    Parámetros:
        datos (dict): Diccionario con el nombre de la ciudad como clave
                      y una lista de temperaturas semanales como valor.
    
    Retorna:
        dict: Diccionario con el nombre de la ciudad y su temperatura promedio.
    """
    promedios = {}
    for ciudad, temperaturas in datos.items():
        promedio = sum(temperaturas) / len(temperaturas)
        promedios[ciudad] = round(promedio, 2)
    return promedios


# ----------------- PRUEBA DEL CÓDIGO ------------------

datos_temperaturas = {
    "Quito": [18, 20, 19, 21],
    "Guayaquil": [28, 30, 29, 31],
    "Cuenca": [15, 16, 14, 17]
}

resultados = calcular_promedio_temperaturas(datos_temperaturas)

print("Promedios de temperatura por ciudad:")
for ciudad, promedio in resultados.items():
    print(f"{ciudad}: {promedio} °C")

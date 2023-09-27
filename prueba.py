from data_stark import lista_personajes

def casteo_datos(lista: list):
    for personajes in lista:
        personajes["peso"] = float(personajes["peso"])
        personajes["fuerza"] = float(personajes["fuerza"])
        personajes["altura"] = float(personajes["altura"])

""" def promedio_peso_masculino(lista: list):
    
    contador_M = 0
    
    acumulador_peso = 0
    
    for personajes in lista_personajes:
        if personajes["genero"] == "M":
            
            acumulador_peso += personajes["peso"]
            
            contador_M += 1
    
    if contador_M != 0:
        promedio_peso_M = acumulador_peso/contador_M
        mensaje = "\nEl promedio de peso de los Héroes masculinos es {0:.2f} \n".format(promedio_peso_M)
    else:
        mensaje ="\nNo hay héroes del género Masculino"
    
    print(mensaje)


promedio_peso_masculino(casteo_datos(lista_personajes)) """

def fuerza_mayor_al_promedio(lista:list):
    
    mensaje = None
    
    acumulador_F = 0
    
    contador_F = 0

    for personajes in lista_personajes:
        
        if personajes["genero"] == "F":

            acumulador_F += personajes["fuerza"]
            
            contador_F  += 1

    if contador_F != 0:
        promedio_F = acumulador_F / contador_F

        for personajes in lista_personajes:
            
            if personajes["fuerza"] > promedio_F:
                nombre = personajes["nombre"]
                peso = personajes["peso"]
                
                mensaje = "\nLos siguientes héroes superan la fuerza promedio del género F..\n"
                mensaje += "\nNombre: {0} \nPeso: {1} \n".format(nombre, peso)
    else:
        mensaje = "\nNo hay héroes femeninos o ningún héroe supera el promedio de fuerza femenino"

    print(mensaje)

fuerza_mayor_al_promedio(casteo_datos(lista_personajes))
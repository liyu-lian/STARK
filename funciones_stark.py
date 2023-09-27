""" A. Recorrer la lista imprimiendo por consola todos los datos de cada superhéroe
B. Recorrer la lista y mostrar la identidad y el peso del superhéroe con mayor
fuerza (MÁXIMO)
C. Recorrer la lista y mostrar nombre e identidad del superhéroe más bajo
(MÍNIMO)
D. Recorrer la lista y determinar el peso promedio de los superhéroes
masculinos (PROMEDIO)
E. Recorrer la lista y mostrar nombre y peso de los superhéroes (cualquier
género) los cuales su fuerza supere a la fuerza promedio de todas las
superhéroes de género femenino """


from data_stark import lista_personajes

def castar_datos(lista: list):
    for personajes in lista:
        personajes["peso"] = float(personajes["peso"])
        personajes["fuerza"] = float(personajes["fuerza"])
        personajes["altura"] = float(personajes["altura"])
        

def mostrar_todo(lista: list):
    for heroe in lista_personajes:

        print(f'''
        Nombre: {heroe['nombre']}
        Identidad: {heroe ['identidad']}
        Empresa: {heroe ['empresa']}
        Altura: {heroe ['altura']}
        Peso: {heroe ['peso']}
        Genero: {heroe ['genero']}
        Color ojos: {heroe ['color_ojos']}
        Color de pelo: {heroe ['color_pelo']}
        Fuerza: {heroe ['fuerza']}
        Inteligencia: {heroe ['inteligencia']}
        ''') 

def calcular_mayor_fuerza(lista: list):
    #B. Recorrer la lista y mostrar la identidad y el peso del superhéroe con mayor fuerza (MÁXIMO)
    
    bandera = 0
    
    for personajes in lista_personajes:
        
        if bandera  == 0 or personajes["fuerza"] > mas_fuerza:
            mas_fuerza = personajes["fuerza"]
            mas_fuerza_identidad =  personajes["identidad"]
            mas_fuerza_peso = personajes["peso"]
            
            bandera = 1
    
    mensaje = "\nEl héroe con más fuerza {0} es {1} con un peso de {2} Kg.\n".format(mas_fuerza, mas_fuerza_identidad, mas_fuerza_peso)
    print(mensaje)
    
def calcular_heroe_mas_bajo (lista: list):
    
    bandera_1 = 0
    
    for personajes in lista_personajes:
        
        if bandera_1 == 0 or personajes["altura"]< menos_altura:
            menos_altura = personajes["altura"]
            identidad_menos_altura =  personajes["identidad"]
            nombre_menos_altura = personajes["nombre"]

        bandera_1 = 1

    mensaje = "\nEl héroe más bajo {0} es {1}, {2} \n".format(menos_altura, nombre_menos_altura, identidad_menos_altura)
    print(mensaje)
    
def calcular_promedio_peso_masculino(lista: list):
    
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
    
    
def calcular_fuerza_mayor_al_promedio(lista:list):
    
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

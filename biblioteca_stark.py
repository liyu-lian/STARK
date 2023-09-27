from data_stark import lista_personajes
from funciones_stark2 import *

def imprimir(funcion):
    """Se encarga de imprimir o mostrar las funciones que no printeen su resultado"""
    print(funcion)

def stark_normalizar_dato(lista: list):
    """ 1.Castea/normaliza los datos de la lista que representen dígitos. Antes verifica que no estén ya en float/int"""

    bandera = False

    for heroe in lista:

        #Valida que el diccionario no esté vacío
        if len(heroe) != 0:

            #valida que el tipo de dato de la key sea string
            if type(heroe["altura"]) == str:

                heroe["altura"] = float(heroe["altura"])

                bandera = True

            if type(heroe["peso"]) == str:

                heroe["peso"] = float(heroe["peso"])

                bandera = True

            if type(heroe["fuerza"]) == str:

                heroe["fuerza"] = int(heroe["fuerza"])

                bandera = True
        
        else:
            bandera= False

    if  bandera == True:

        print("Datos normalizados")
    else:
        print("Hubo un error al normalizar los datos.\
Verifique que la lista no este vacía o que los datos ya no\
se hayan normalizado anteriormente.")

    return lista_personajes

def obtener_dato(heroe: dict, clave: str):
    """2.Valida que el diccionario no esté vacío y que la key insertada exista dentro del mismo"""

    dato_validado =  False

    if len(heroe) != 0 and clave in heroe:
        dato_validado = heroe[clave]
    else:
        print("El diccionario está vacío o la clave a obtener no existe.. ")

    return dato_validado

def obtener_nombre(heroe: dict, clave: str):
    """3.Toma un diccionario junto a una key y valida que esa key exista en dicho diccionario para luego mostrarla"""

    nombre = obtener_dato(heroe, clave)
    nombre_obtenido = f"Nombre: {nombre}"

    return nombre_obtenido

def obtener_nombre_y_dato(heroe: dict, clave: str)->str:
    """4.obtiene el nombre de un diccionario y una key a elección retornando un str con ambas. Además, un booleano"""
    nombre = obtener_nombre(heroe, "nombre")
    dato = obtener_dato(heroe, clave)
    nombre_dato = f"Nombre: {nombre} | {clave}: {dato}\n"

    return nombre_dato

def obtener_maximo(heroes: list, clave: str):
    """5.Busca el maximo con una clave específica de una lista"""
    flag_max = True

    if len(heroes) != 0:
        for heroe in heroes:
            if type(heroe[clave]) == float or type(heroe[clave]) == int:
                if flag_max == True or heroe[clave] > maximo:

                    maximo = heroe[clave]
                    nombre_max = obtener_nombre(heroe, "nombre")
                    flag_max = False

        mensaje = f"El maximo en {clave} es {maximo}. {nombre_max}"
    else:
        mensaje  = "no hay datos para calcular el maximo.. "


    return mensaje

def obtener_minimo(heroes: list, clave: str):
    """6.Busca el minimo con una clave específica de una lista"""
    flag = False
    flag_min = True

    if len(heroes) != 0:
        for heroe in heroes:
            if type(heroe[clave]) == float or type(heroe[clave]):
                if flag_min == True or heroe[clave] < minimo:
                    minimo = heroe[clave]
                    nombre_min= obtener_nombre(heroe, "nombre")
                    flag_min = False

                flag = True

        mensaje = f"El minimo en {clave} es {minimo}. {nombre_min}"
    else:
        mensaje  = "no hay datos para calcular el minimo.. "

    print(mensaje)

    return minimo

def obtener_dato_cantidad(lista: list, numero, clave: str):
    """7.Devuelve una lista de diccionarios que coincidan con el maximo o el minimo de una clave"""

    lista_coincidentes = []

    if numero == 1:
        caso = obtener_maximo(lista, clave)
    elif numero == 2:
        caso = obtener_minimo(lista, clave)

    for heroe in lista:
        if heroe[clave] == caso:
            lista_coincidentes.append(heroe)

    return lista_coincidentes

def stark_imprimir_heroes(lista: list):
    """8.Imprime todos los diccionarios de los heroes """
    flag = False

    if len(lista) != 0:

        for heroe in lista:
            mensaje = f'''
Nombre: {heroe['nombre']}
Identidad: {heroe ['identidad']}
Empresa: {heroe ['empresa']}
Altura: {heroe ['altura']:.2f}
Peso: {heroe ['peso']:.2f}
Genero: {heroe ['genero']}
Color ojos: {heroe ['color_ojos']}
Color de pelo: {heroe ['color_pelo']}
Fuerza: {heroe ['fuerza']}
Inteligencia: {heroe ['inteligencia']}
''' 
        flag = True

    print(flag)

    return mensaje

def sumar_dato_heroe(heroes: list, dato:str):
    """9.Suma los valores de una clave específica (ejemplo: Fuerza, peso, altura.)"""
    acumulador_dato = 0

    for heroe in heroes:
        if dato in heroe:
            datos = obtener_dato(heroe, dato)
            acumulador_dato += datos
        else:
            acumulador_dato = 0

    return acumulador_dato

def  dividir(dividendo, divisor):
    """10.Divide dos valores ingresados"""
    flag = False

    if divisor != 0:
        resultado_division = dividendo/divisor
        flag = True
    else:
        print("No se puede realizar la división")

    return resultado_division

def calcular_promedio(heroes: list, dato: str):
    """11.Calcula el promedio de la lista y dato(Ejemplo: Fuerza, altura, peso) ingresado"""
    mostrar_promedio_dato(heroes, dato)
    suma_dato = sumar_dato_heroe(heroes, dato)
    cantidad = len(heroes)
    promedio = dividir(suma_dato, cantidad)

    print(f"El promedio de {dato} es.. {promedio}")

def mostrar_promedio_dato(lista: list, dato: str):
    """12.valida que la lista ingresada no está vacía y que la key es float o int."""
    flag = False

    if len(lista) != 0:
        for diccionarios in lista:
            if type(diccionarios[dato]) == float or type(diccionarios[dato]) == int:
                flag = True

    return flag

# ----------PARTE DEL MENU DE LAS CONSIGNAS DE STARK 2-----------

def mostrar_menu():

    menu = (f"""----------Menu de opciones----------\n
1- Normalizar datos de la lista (deberá hacer este paso antes de avanzar)
2-Héroes no binarios
3-Héroe Femenino más alto
4-Héroe masculino más alto
5-héroe más débil masculino
6-héroe más débil no binario
7-Fuerza promedio de los héroes de género NB
8-Todos los colores de ojo
9-Todos los colores de pelo
10-Grupos de héroes por su color de ojos
11-Grupos de héroes por su inteligencia

Presiones '0' para salir..

""")

    return menu

def validar_entero(entero: str):
    """ Verifica que el str ingresado sea un valor numérico, devolviendo así un bool que indique con 'True' si se pudo llevar a cabo la validación."""

    flag = False

    if entero.isdigit():
        flag = True

    return flag

def stark_menu_principal():
    """Verifica que el str ingresado sea de caracter numérico dando paso a la instancia de opciones las cuales ejecutaran sus respectivas funciones"""

    opciones = input(mostrar_menu())
    flag_validada = validar_entero(opciones)

    if flag_validada == True:
        opciones = int(opciones)
    else:
        print("Error. Ingrese un número acorde a las opciones.. ")

    return opciones

def stark_marvel_app(lista: list):

    flag_casteo = False

    while True:
        opciones = stark_menu_principal()

        if opciones == 0:
            break
        elif opciones == 1:
            lista_casteada = stark_normalizar_dato(lista_personajes)
            flag_casteo = True
        else:
            if flag_casteo == True:
                match opciones:
                    case 2:
                        mostrar_por_genero(lista_casteada, "genero", "NB")
                    case 3:
                        imprimir(mostrar_alto_por_genero(lista_casteada,"genero","F"))
                    case 4:
                        imprimir(mostrar_alto_por_genero(lista_casteada,"genero","M"))
                    case 5:
                        imprimir(mostrar_debil_por_genero(lista_casteada,"genero","M"))
                    case 6:
                        imprimir(mostrar_debil_por_genero(lista_casteada,"genero","NB"))
                    case 7:
                        imprimir(mostrar_promedio_fuerza_nb(lista_casteada,"genero","NB"))
                    case 8:
                        mostrar_por_color(lista_personajes,"color_ojos")
                    case 9:
                        mostrar_por_color(lista_personajes,"color_pelo")
                    case 10:
                        listado_por_caracteristica(lista_personajes, "color_ojos")
                    case 11:
                        listado_por_caracteristica(lista_personajes, "inteligencia")
            else:
                print(f"Error. No puede utilizar las opciones sin antes castear.\
Presione 1 para castear los datos o presione s para salir")

#--------- FUNCIONES STARK 2 -----------

def mostrar_por_genero(lista:list, key: str, genero: str):
    lista_genero = []

    for personajes in lista:

        if personajes[key] == genero:
            nombre = obtener_nombre(personajes, "nombre")
            lista_genero.append(personajes)

            print(nombre)

    return lista_genero

def mostrar_alto_por_genero(lista: list, key: str, genero: str):
    lista_gen = mostrar_por_genero(lista,key,genero)
    mas_alto = obtener_maximo(lista_gen,"altura")

    return mas_alto

def mostrar_debil_por_genero(lista: list, key: str, genero: str):
    lista_genero = mostrar_por_genero(lista,key,genero)
    mas_debil = obtener_minimo(lista_genero,"fuerza")

    return mas_debil

def mostrar_promedio_fuerza_nb(lista: list, key: str, genero: str):
    lista_genero = mostrar_por_genero(lista,key,genero)
    promedio_fuerza_nb = calcular_promedio(lista_genero,"fuerza")

    return promedio_fuerza_nb

def mostrar_por_color(lista: list, clave: str):
    diccionario_caracteristica = {}

    for heroe in lista:

        if clave in heroe:

            if not heroe[clave] in diccionario_caracteristica:
                diccionario_caracteristica[heroe[clave]] = 1
            else:
                diccionario_caracteristica[heroe[clave]] += 1
        else:
            print("La clave no está dentro del diccionario..")

    #items() --> muestra las key-valores dentro de un diccionario
    for colores, cantidad in diccionario_caracteristica.items():
        print(f"{colores}: {cantidad}")

    return diccionario_caracteristica

def listado_por_caracteristica(lista: list, clave: str):
    diccionario = mostrar_por_color(lista, clave)
    
    for caracteristica in list(diccionario.keys()):
        mensaje = f"\nLos superhéroes con {clave} '{caracteristica}' son:"
        print(mensaje)

        for heroe in lista:
            if heroe[clave] == caracteristica:
                print(f"- {heroe['nombre']}")



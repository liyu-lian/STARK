from data_stark import lista_personajes
import re

def imprimir(funcion):
    """Se encarga de imprimir o mostrar las funciones que no printeen su resultado"""
    print(funcion)

def stark_normalizar_dato(lista: list) -> list:
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

def obtener_dato(lista: list, clave: str) -> list:
    """Recibe una lista y una clave(str). Busca obtener el valor cargado en la key con el mismo nombre que la clave"""
    lista = stark_normalizar_dato(lista)

    flag = False
    
    lista_clave = []

    for heroe in lista:
        if clave in heroe and len(clave) != 0:
            info_clave = heroe[clave]
            lista_clave.append(info_clave)

            flag = True

    print(flag)

    return lista_clave

def validar_tipo(dato, tipo):
    """ Valida que la key específica dentro de una lista o el dato insertado no esté vacío y sea STR """
    flag = False

    if type(dato) == tipo:
        flag = True
    else:
        dato = False

    print(flag)

    return dato

def extraer_iniciales(nombre_heroe: str) -> str:
    """ Obtiene un nombre y retorna sus iniciales separadas por puntos """

    nombre_heroe = validar_tipo(nombre_heroe, str)

    iniciales = []

    if "-" in nombre_heroe:
        nombre_heroe = re.sub("-", " ", nombre_heroe)

    if "the" in nombre_heroe:
        nombres = re.split("the", nombre_heroe)
    else:
        nombres = re.split(" ", nombre_heroe)

    for n in nombres:
        iniciales.extend(re.findall(r'\b\w', n))

    union_iniciales = ".".join(iniciales) +"."

    return union_iniciales

def obtener_dato_formato(dato: str) -> str:
    dato = validar_tipo(dato, str)

    if dato != False:
        dato = dato.lower()
        dato = re.sub(" ", "_", dato)
    else:
        print("No se pudo realizar el procedimiento.. Revise que los datos insertados sean correctos")

    return dato

def stark_imprimir_nombre_con_iniciales(nombre_heroe: str):
    nombre_heroe = validar_tipo(nombre_heroe, dict)

    if nombre_heroe != False:
        



lista_clave = obtener_dato(lista_personajes, "nombre")

imprimir(obtener_dato_formato(lista_clave[0]))






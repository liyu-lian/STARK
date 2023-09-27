""" A. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de
género NB
B. Recorrer la lista y determinar cuál es el superhéroe más alto de género F
C. Recorrer la lista y determinar cuál es el superhéroe más alto de género M
D. Recorrer la lista y determinar cuál es el superhéroe más débil de género M
E. Recorrer la lista y determinar cuál es el superhéroe más débil de género NB
F. Recorrer la lista y determinar la fuerza promedio de los superhéroes de
género NB
G. Determinar cuántos superhéroes tienen cada tipo de color de ojos.
H. Determinar cuántos superhéroes tienen cada tipo de color de pelo.
I. Listar todos los superhéroes agrupados por color de ojos.
J. Listar todos los superhéroes agrupados por tipo de inteligencia """

from data_stark import lista_personajes

def casteo_datos(lista:list):
    for personajes in lista_personajes:
        personajes["peso"] = float(personajes["peso"])
        personajes["fuerza"] = float(personajes["fuerza"])
        personajes["altura"] = float(personajes["altura"])

def mostrar_no_binarios(lista:list):
    mensaje = None

    for personajes in lista_personajes:

        if personajes["genero"] == "NB":
            mensaje = "Nombre: {0}\n".format(personajes["nombre"])

            print(mensaje)

def mostrar_heroe_mas_alto_f(lista: list):
    mensaje = None

    bandera = 0

    for personajes in lista_personajes:
        if personajes["genero"] == "F":
            if bandera  == 0 or personajes["altura"] > mas_altura:
                mas_altura = personajes["altura"]
                mas_altura_nombre =  personajes["nombre"]
                
                bandera = 1
        
    mensaje = "El héroe femenino más alto es: {0}. Con altura de {1}".format(mas_altura_nombre, mas_altura)
    print(mensaje)

def mostrar_heroe_mas_alto_m(lista: list):
    mensaje = None

    bandera = 0

    for personajes in lista_personajes:
        if personajes["genero"] == "M":
            if bandera  == 0 or personajes["altura"] > mas_altura:
                mas_altura = personajes["altura"]
                mas_altura_nombre =  personajes["nombre"]
                
                bandera = 1
        
    mensaje = "El héroe masculino más alto es: {0}. Con altura de {1:.1f}".format(mas_altura_nombre, mas_altura)
    print(mensaje)

def mostrar_mas_debil_m(lista:list):
    mensaje = None

    bandera_ = 0

    for personajes in lista_personajes:
        if personajes["genero"] == "M":
            if bandera_  == 0 or personajes["fuerza"] <  menos_fuerza:
                menos_fuerza = personajes["fuerza"]
                menos_fuerza_nombre =  personajes["nombre"]
                
                bandera_ = 1
    
    mensaje = "El héroe masculino más débil es: {0}. Con una fuerza de {1}".format(menos_fuerza_nombre, menos_fuerza)
    print(mensaje)

def mostrar_mas_debil_nb(lista:list):
    mensaje = None

    bandera_ = 0

    for personajes in lista_personajes:
        if personajes["genero"] == "NB":
            if bandera_  == 0 or personajes["fuerza"] <  menos_fuerza:
                menos_fuerza = personajes["fuerza"]
                menos_fuerza_nombre =  personajes["nombre"]
                
                bandera_ = 1
    
    mensaje = "El héroe no binario más débil es: {0}. Con una fuerza de {1}".format(menos_fuerza_nombre, menos_fuerza)
    print(mensaje)

def mostrar_promedio_fuerza_nb(lista: list):

    mensaje = None

    acumulador_nb = 0

    contador_nb = 0

    for personajes in lista_personajes:

        if personajes["genero"] == "NB":
            acumulador_nb += personajes["fuerza"]

            contador_nb += 1
    
    if contador_nb != 0:
        promedio_fuerza_nb = acumulador_nb / contador_nb
        mensaje = "\nPromedio de fuerza de los superhéroes de género NB: {0:.2f}".format(promedio_fuerza_nb)
    else:
        mensaje = "\nNo hay héroes no binarios.. "

    print(mensaje)

def mostrar_colores_ojos(lista: list):
    mensaje = 0

    contador_yellow = 0
    contador_brown = 0
    contador_blue = 0
    contador_green = 0
    contador_hazel = 0
    contador_silver = 0
    contador_red = 0    

    for i in lista_personajes:
        color_ojos = i["color_ojos"]

        match color_ojos:
            case "Yellow" | "Yellow (without irises)":
                contador_yellow += 1
            case "Brown":
                contador_brown += 1
            case "Blue":
                contador_blue += 1
            case "Green":
                contador_green += 1
            case "Hazel":
                contador_hazel += 1
            case "Silver":
                contador_silver += 1
            case "Red":
                contador_red += 1

    mensaje = "\nColores de ojos y la cantidad de quien los tiene..\n"
    mensaje += f""" 
    Ojos amarillos con y sin irises: {contador_yellow}
    Ojos marrones: {contador_brown}
    Ojos azules: {contador_blue}
    Ojos verdes: {contador_green}
    Ojos hazel: {contador_hazel}
    Ojos plateados: {contador_silver}
    Ojos rojos: {contador_red}
    """
    print(mensaje)

def mostrar_colores_pelo(lista: list):
    mensaje = 0

    contador_white = 0
    contador_yellow = 0
    contador_brown = 0
    contador_green = 0
    contador_auburn = 0
    contador_blond = 0
    contador_red = 0    
    contador_black = 0
    contador_sinpelo = 0

    for i in lista_personajes:
        colores_pelo = i["color_pelo"]

        match colores_pelo:
            case "Yellow":
                contador_yellow += 1
            case "Brown" | "Brown / White":
                contador_brown += 1
            case "Black":
                contador_black += 1
            case "Green":
                contador_green += 1
            case "White":
                contador_white += 1
            case "Auburn":
                contador_auburn += 1
            case "Blond":
                contador_blond += 1
            case "Red" | "Red / Orange":
                contador_red += 1
            case "No Hair" | "":
                contador_sinpelo += 1

    mensaje = "\nEstilo de pelo y la cantidad de quien los tiene..\n"
    mensaje += f""" 
    Pelo amarillo: {contador_yellow}
    Pelo marron: {contador_brown}
    Pelo negro: {contador_black}
    Pelo verde: {contador_green}
    Pelo blanco: {contador_white}
    Pelo auburn: {contador_auburn}
    Pelo Rubio: {contador_blond}
    Pelo rojo: {contador_red}
    Pelón: {contador_sinpelo}
    """
    print(mensaje)

def mostrar_listado(lista:list):
    Nombre: {lista['nombre']}
    Identidad: {lista ['identidad']}
    Empresa: {lista ['empresa']}
    Altura: {lista ['altura']}
    Peso: {lista ['peso']}
    Genero: {lista ['genero']}
    Color_ojos: {lista ['color_ojos']}
    Color_de_pelo: {lista ['color_pelo']}
    Fuerza: {lista ['fuerza']}
    Inteligencia: {lista ['inteligencia']}

def mostrar_listado_ojos(lista: list):
    
    mensaje =  None

    lista_amarillo = []
    lista_marron = []
    lista_azul = []
    lista_verde = []
    lista_hazel = []
    lista_plateado = []
    lista_rojo = []

    for i in lista_personajes:

        color_ojos = i["color_ojos"]

        match color_ojos:
            case "Yellow" | "Yellow (without irises)":
                lista_amarillo.append(i["nombre"])
            case "Brown":
                lista_marron.append(i["nombre"])
            case "Blue":
                lista_azul.append(i["nombre"])
            case "Green":
                lista_verde.append(i["nombre"])
            case "Hazel":
                lista_hazel.append(i["nombre"])
            case "Silver":
                lista_plateado.append(i["nombre"])
            case "Red":
                lista_rojo.append(i["nombre"])

    mensaje = f"""\nHéroes agrupados segun su color de ojos:
    Ojos amarillos:
        {lista_amarillo}
    Ojos marron:
        {lista_marron}
    Ojos azul:
        {lista_azul}
    Ojos verde:
        {lista_verde}
    Ojos hazel:
        {lista_hazel}
    Ojos Silver:
        {lista_plateado}
    Ojos rojos:
        {lista_rojo}
    """  
    print(mensaje)

def mostrar_listado_inteligencia(lista: list):

    lista_good = []
    lista_high = []
    lista_average = []
    lista_= []

    for i in lista_personajes:
        inteligencia = i["inteligencia"]

        match inteligencia:
            case "good":
                lista_good.append(i["nombre"])
            case "average":
                lista_average.append(i["nombre"])
            case "high":
                lista_high.append(i["nombre"])
            case "":
                lista_.append(i["nombre"])
    
    mensaje = f"""\nHéroes agrupados segun su tipo de inteligencia:
        Good:
        {lista_good}
        High:
        {lista_high}
        Average:
        {lista_average}
        No tiene:
        {lista_}
    """  
    print(mensaje)

"""I. Listar todos los superhéroes agrupados por color de ojos.
J. Listar todos los superhéroes agrupados por tipo de inteligencia """

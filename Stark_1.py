from funciones_stark import *


while True:

    print("MENU DE OPCIONES")
    opcion = input("""\n
A-Mostrar todos los datos
B-Héroe con mayor fuerza
C-Héroe más bajo
D-Peso promedio Héroes masculinos
E-Super Héroe  con fuerza mayor al promedio
Presione S para salir.. 
""")
    
    match opcion:
        case 's':
            break
        case 'a':
            mostrar_todo(castar_datos(lista_personajes))
        case 'b':
            calcular_mayor_fuerza(castar_datos(lista_personajes))
        case 'c':
            calcular_heroe_mas_bajo(castar_datos(lista_personajes))
        case 'd':
            calcular_promedio_peso_masculino(castar_datos(lista_personajes))
        case 'e':
            calcular_fuerza_mayor_al_promedio(castar_datos(lista_personajes))

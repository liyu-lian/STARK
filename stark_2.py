from data_stark import lista_personajes
from funciones_stark2 import *

while True:

    print("MENU DE OPCIONES")
    opcion = input("""\n
A-Héroes no binarios
B-Héroe Femenino más alto
C-Héroe masculino más alto
D-héroe más débil masculino
E-héroe más débil no binario
F-Fuerza promedio de los héroes de género NB
G-Todos los colores de ojo
H-Todos los colores de pelo
I-Grupos de héroes por su color de ojos
J-Grupos de héroes por su inteligencia
Presione S para salir..
    """)


    match opcion:
        case 's':
            break
        case 'a':
            mostrar_no_binarios(lista_personajes)
        case 'b':
            mostrar_heroe_mas_alto_f(casteo_datos(lista_personajes))
        case 'c':
            mostrar_heroe_mas_alto_m(casteo_datos(lista_personajes))
        case 'd':
            mostrar_mas_debil_m(casteo_datos(lista_personajes))
        case 'e':
            mostrar_mas_debil_nb(casteo_datos(lista_personajes))
        case 'f':
            mostrar_promedio_fuerza_nb(casteo_datos(lista_personajes))
        case 'g':
            mostrar_colores_ojos(lista_personajes)
        case 'h':
            mostrar_colores_pelo(lista_personajes)
        case 'i':
            mostrar_listado_ojos(lista_personajes)
        case 'j':
            mostrar_listado_inteligencia(lista_personajes)




import Ingresar_usuario
while True:
    print ("""
        -----------------
          THE CHACHIPUN  
        -----------------
    """)
    usuarios = []
    print("BIENVENID@! Que te gustaria hacer?")
    print("1. Ingresar usuario")
    print("2. Jugar multijugador")
    print("3. Jugar contra IA")
    print("4. Puntajes obtenidos")

    opcion = input("Ingresa una opcion -> ")

    if opcion == "1":
        Ingresar_usuario.info(usuarios)

        break
    else: 
        print("Ingresaste una respuesta INCORRECTA, Intenta de nuevo")
        input("Presiona ENTER para continuar -> ")

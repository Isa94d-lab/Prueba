def info(usuarios):
    nombre_delusuario = input("Ingresa tu nombre completo -> ")
    nickname_delusuario = input ("Ingresa tu nickname -> ")
    usuarios.append({
        'nombre': nombre_delusuario,
        'nickname': nickname_delusuario
    })
    print("usuarios")
    pass 
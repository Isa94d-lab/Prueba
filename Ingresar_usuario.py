def info(usuarios):
    print("""
    -----------------------------
         REGISTRO DE USUARIO     
    -----------------------------
    """)
    while True:
        def nombre_delusuario ():
            pass  
        def nickname_delusuario ():
            pass 
        usuarios.append({
            'nombre': nombre_delusuario,
            'nickname': nickname_delusuario
        })
        nombre_delusuario = input("Ingresa tu nombre completo -> ")
        nickname_delusuario = input ("Ingresa tu nickname -> ")
        if nickname_delusuario == usuarios['nickname']:
            print("Este nickname YA ESTA REGISTRADO, Ingresa uno diferente")
            w= input("Preciona ENTER para continuar -> ")
            return 
        else: 
            print({usuarios})
            break
from cursor_del_pool import obtenercursor
from usuarios import usuario
from usuarioDao import usuariodao
from logger_base import log

valor = int(input(f'''1.listar usuarios
2. agregar usuario 
3. actualizar usuario 
4. eliminar usuario
5. salir
selecione un numero: '''))
while valor != 5:
    if valor == 1:
        usuarios1 = usuariodao.selecionar()
        for usuarioo in usuarios1:
            print(usuarioo.id, usuarioo.user)
    elif valor == 2:
        nombre = input(f'User:')
        password = input(f'Password:')
        Usuario = usuario(user=nombre, passw=password)
        usuariodao.insertar(Usuario)
    elif valor == 3:
        id = input(f'ingrese el id del usuario que desea actualizar:')
        PasswordActual = input(f'ingrese password (tenga cuidado con los espacios): ')
        with obtenercursor() as cursor:
            query = 'SELECT * FROM usuarios WHERE id_usuario=%s'
            cursor.execute(query, (id,))
            registro = cursor.fetchone()
            if registro[2] == PasswordActual:
                NuevoUser = input(f'ingrese nuevo user:')
                NuevoPassword = input(f'ingrese nuevo password: ')
                Usuario = usuario(id=id, user=NuevoUser, passw=NuevoPassword)
                usuariodao.actualizar(Usuario)
            else:
                log.error(f'Password incorreto')
    elif valor == 4:
        id = int(input(f'ingrese el id del usuario que desea eliminar:'))
        PasswordA = input(f'ingrese password (tenga cuidado con los espacios): ')
        with obtenercursor() as cursor:
            query = 'SELECT * FROM usuarios WHERE id_usuario=%s'
            cursor.execute(query, (id,))
            registro = cursor.fetchone()

            if registro[2] == PasswordA:
                Usuario = usuario(id=id)
                usuariodao.eliminar(Usuario)
            else:
                log.error(f'Password incorreto')

    valor = int(input(f'''
    1.listar usuarios
    2. agregar usuario 
    3. actualizar usuario 
    4.eliminar usuario
    5.salir
    selecione un numero: '''))

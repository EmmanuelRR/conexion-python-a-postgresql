from cursor_del_pool import obtenercursor
from usuarios import usuario
from logger_base import log

class usuariodao:
    SELECIONAR='SELECT * FROM usuarios'
    INSERTAR= 'INSERT INTO usuarios(username,password) VALUES(%s, %s)'
    ACTUALIZAR='UPDATE usuarios SET username=%s, password= %s WHERE id_usuario=%s'
    ELIMINAR='DELETE FROM usuarios  WHERE id_usuario=%s'

    @classmethod
    def selecionar(cls):
        with obtenercursor() as cursor:
            cursor.execute(cls.SELECIONAR)
            registros=cursor.fetchall()
            usuarioss=[]
            for registro in registros:
                usuario1= usuario(registro[0], registro[1], registro[2])
                usuarioss.append(usuario1)
            return usuarioss
    @classmethod
    def insertar(cls,usuario):
        with obtenercursor() as cursor:
            valores=(usuario.user, usuario.passw)
            cursor.execute(cls.INSERTAR, valores)
            log.info(f'usuario actualizado: {usuario}')
            return cursor.rowcount

    @classmethod
    def actualizar(cls, usuario):
        with obtenercursor() as cursor:
            valores = (usuario.user, usuario.passw, usuario.id)
            cursor.execute(cls.ACTUALIZAR, valores)
            log.info(f'usuario actualizado: {usuario}')
            return cursor.rowcount

    @classmethod
    def eliminar(cls, usuario):
        with obtenercursor() as cursor:
            valores = (usuario.id,)
            cursor.execute(cls.ELIMINAR, valores)
            log.info(f'usuario eliminado: {usuario}')
            return cursor.rowcount

if __name__== '__main__':
    usuario1=usuario(user='rxn', passw = 'coldplay')
    usuariodao.insertar(usuario1)
    usuarios1=usuariodao.selecionar()
    for usuarioo in usuarios1:
        log.debug(usuarioo)
from conexion import conexion
from logger_base import log
class obtenercursor:
    def __init__(self):
        self._conexion = None
        self.cursor = None
    def __enter__(self):
        log.debug('inicio del metodo with ')
        self._conexion= conexion.obterconexion()
        self.cursor= self._conexion.cursor()
        return self.cursor
    def __exit__(self, exc_type, exc_val, exc_tb):
        log.debug('se ejecuta metodo exit')
        if exc_val:
            self._conexion.rollback()
            log.error(f'ocucrrio un error: {exc_val} {exc_tb}')
        else:
            self._conexion.commit()
            log.debug('commit de la transaccion')
        self.cursor.close()
        conexion.liberarConexion(self._conexion)

if __name__== '__main__':
    with obtenercursor() as cursor:
        log.debug('dentro del bloque with')
        cursor.execute('SELECT * FROM usuarios')
        log.debug(cursor.fetchall())



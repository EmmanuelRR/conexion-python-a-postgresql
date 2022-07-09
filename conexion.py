from logger_base import log
import sys
from psycopg2 import pool

class conexion:
    _DATABASE= 'usuario'
    _USERNAME= 'postgres'
    _PASSWORD= 'admin'
    _DB_PORT= '5432'
    _HOST = '127.0.0.1'
    _MIN_CON = '1'
    _MAX_CON = '5'
    _POOL= None

    @classmethod
    def obtenerPool(cls):
        if cls._POOL is None:
            try:
                cls._POOL= pool.SimpleConnectionPool(cls._MIN_CON, cls._MAX_CON,
                                                     host=cls._HOST,
                                                     user= cls._USERNAME,
                                                     password=cls._PASSWORD,
                                                     port= cls._DB_PORT,
                                                     database=cls._DATABASE)
                log.debug(f'Creacion del pool exitosa: {cls._POOL}')
                return cls._POOL
            except Exception as e:
                log.error(f'ocurrio un error al obtener el pool: {e}')
                sys.exit()
        else:
            return cls._POOL

    @classmethod
    def obterconexion(cls):
        conexion= cls.obtenerPool().getconn()
        log.debug(f'conexion obtenida del pool : {conexion}')
        return conexion
    @classmethod
    def liberarConexion(cls,conexion):
        cls.obtenerPool().putconn(conexion)
if __name__== '__main__':
    conexion1= conexion.obterconexion()
    conexion2= conexion.obterconexion()
from capa_datos_usuario.cursor_del_pool import CursorDelPool
from capa_datos_usuario.usuario import Usuario
from capa_datos_usuario.conexion import Conexion
from logger_base import log

class UsuarioDAO:
    """
    DAO significa: Data Access Object
    CRUD significa:
                    Create -> Insertar
                    Read   -> Seleccionar
                    Update -> Actualizar
                    Delete -> Eliminar
    """
    _SELECCIONAR = 'SELECT * FROM usuario ORDER BY id_usuario'
    _INSERTAR = 'INSERT INTO usuario(username, password) VALUES (%s, %s)'
    _ACTUALIZAR = 'UPDATE usuario SET username=%s, password=%s WHERE id_usuario=%s'
    _ELIMINAR = 'DELETE FROM usuario WHERE id_usuario=%s'

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            usuarios = []
            for registro in registros:
                usuario = Usuario(registro[0], registro[1], registro[2])
                usuarios.append(usuario)
            return usuarios
    @classmethod
    def insertar(cls, usuario):
        with CursorDelPool() as cursor:
            valores = (usuario.username, usuario.password)
            cursor.execute(cls._INSERTAR, valores)
            log.debug(f'Usuario insertado: {usuario}')
            return cursor.rowcount
    @classmethod
    def actualizar(cls, usuario):
        with CursorDelPool() as cursor:
            valores = (usuario.username, usuario.password, usuario.id_usuario)
            cursor.execute(cls._ACTUALIZAR, valores)
            log.debug(f'Usuario actualizado: {usuario}')
            return cursor.rowcount

if __name__ == '__main__':
    # Actualizar un registro
    usuario1 = Usuario(10, 'Cascara', '332')
    usuario_actualizado = UsuarioDAO.actualizar(usuario1)
    log.debug(f'Usuario actualizado: {usuario_actualizado}')


    # Insertar un registro
    # usuario1 = Usuario(username='Daniel', password='678')
    # usuario_insertado = UsuarioDAO.insertar(usuario1)
    # log.debug(f'Usuario insertado: {usuario_insertado}')

    # Seleccionar objectos
    # usuarios = UsuarioDAO.seleccionar()
    # for usuario in usuarios:
    #    log.debug(usuario)
import sqlite3

class Base_de_datos:
    def __init__(self, puntajes):
        self.conexion = sqlite3.connect(puntajes)
        self.cursor = self.conexion.cursor()

    def crear_tabla(self):
        sentencia = """ 
                    create table if not exists Puntajes
                    (
                        nombre text,
                        puntaje integer
                    )          
                    """
        self.cursor.execute(sentencia)

    def ingresar_puntaje(self, nombre, puntaje):
        sentencia = """ 
                    insert into Puntajes(nombre , puntaje) values(?, ?)                              
                    """
        self.cursor.execute(sentencia, (nombre, puntaje))
        self.conexion.commit()

    def obtener_puntajes(self):
        sentencia = """ 
                    select * from Puntajes order by puntaje desc limit 3
                    """
        self.cursor.execute(sentencia) 
        lista_top_3 = []
        for fila in self.cursor:
            puntaje = {"Nombre": fila[0], "Puntaje": fila[1]}
            lista_top_3.append(puntaje)

        return lista_top_3

    def cerrar_conexion(self):
        self.cursor.close()
        self.conexion.close()
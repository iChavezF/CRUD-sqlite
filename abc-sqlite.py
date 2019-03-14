import sqlite3,time
import subprocess as sp

"""
Codigo fuente de la BD para interactuar con ella
"""


def create_table():
    # Conexion a sqlite3
    conn = getConexion()

    # Asigno cursor de la conexion a una variable local
    cursor = conn.cursor()

    # Defino la consulta de SQL para crear la tabla estudiantes
    query = '''
        CREATE TABLE IF NOT EXISTS student(
        id INTEGER PRIMARY KEY,
        roll INTEGER,
        name TEXT,
        phone TEXT
        );'''

    cursor.execute(query)
    #cursor.execute("-SQL QUERYS")

    # Consignar ala BD las instrucciones que se acaban de ejecutar
    conn.commit()

    # Cerrar conexion
    conn.close()


def add_student(id_,roll, name, phone):
    # Abrir la conexion
    conn = getConexion()
    # Asigna cursor de la bd a una variable local
    cursor = conn.cursor()

    # Query a ejecutar

    query = '''
        INSERT INTO student(id,roll,name,phone)
        VALUES(?,?,?,?)
        '''

    # Ejecuto la conexion en el cursor devuelto por la BD
    cursor.execute(query,(id_,roll,name,phone))

    # Consignar a la Bd la instruccion SQL ejecutada.
    conn.commit()

    # Cerrar conexion
    conn.close()


def get_students():
    # Abrir conexion a BD
    conn = getConexion()

    # Asigno el cursor
    cursor = conn.cursor()

    # Query para ejecutar
    query = '''
        SELECT id,roll, name, phone FROM student
        '''
    # Ejecutar el query
    cursor.execute(query)

    # Obtener el resultado del cursor de los registros y los
    # asigno a una variable
    all_rows = cursor.fetchall()

    # Consigno la consulta a la conexion a la BD
    conn.commit()

    # Cerrar la conexion
    conn.close()

    # Regreso el conjunto de datos devueltos por la consulta
    return all_rows


def get_student_by_id(id_):
    # Traer la conexion desde el metodo GetConexion
    conn = getConexion()

    # Asignar el cursor a una variable local
    cursor = conn.cursor()

    # Query a ejecutar
    query = '''
        SELECT id,roll, name,phone FROM student 
        WHERE id = {}
        '''.format(id_)

    # Ejecutar el QUERY
    cursor.execute(query)

    # Obtener el resultado del cursor de los registros y los
    # asigno a una variable
    all_rows = cursor.fetchall()

    # Consigno la consulta a la conexion a la BD
    conn.commit()

    # Cerrar la conexion
    conn.close()

    # Regreso el conjunto de datos devueltos por la consulta
    return all_rows


def update_student(roll, name, phone):
    # Traer la conexion desde el metodo GetConexion
    conn = getConexion()

    # Asignar el cursor a una variable local
    cursor = conn.cursor()

    # Query a ejecutar
    query = '''
        UPDATE student SET name = ?, phone = ? WHERE roll = ?
        '''

    # Ejecutar el QUERY
    cursor.execute(query, (name, phone, roll))

    # Obtener el resultado del cursor de los registros y los
    # asigno a una variable
    #all_rows = cursor.fetchall()

    # Consigno la consulta a la conexion a la BD
    conn.commit()

    # Cerrar la conexion
    conn.close()

    # Regreso el conjunto de datos devueltos por la consulta
    # return all_rows


def delete_student(id__):
    # Traer la conexion desde el metodo GetConexion
    conn = getConexion()

    # Asignar el cursor a una variable local
    cursor = conn.cursor()

    # Query a ejecutar
    query = '''
        DELETE FROM student WHERE id = {}
        '''.format(id__)

    # Ejecutar el QUERY
    cursor.execute(query)

    # Obtener el resultado del cursor de los registros y los
    # asigno a una variable
    #all_rows = cursor.fetchall()

    # Consigno la consulta a la conexion a la BD
    conn.commit()

    # Cerrar la conexion
    conn.close()

    # Regreso el conjunto de datos devueltos por la consulta
    # return all_rows


def getConexion():
    conn = sqlite3.connect("testdb2.sqlite")
    return conn


def add_data(id_,roll, name, phone):
    add_student(id_,roll, name, phone)


def get_data():
    return get_students()


def show_data():
    students = get_data()
    for students in students:
        print(students)


def show_data_by_id(id_):
    students = get_student_by_id(id_)
    if not students:
        print("No hay registros para el id %r" % id_)
        time.sleep(2)
    else:
        print(students)
        time.sleep(2)



def select():
    create_table()
    sp.call('cls', shell=True)
    sel = input("1. Add\n2. Show\n3. Search\n4. Update\n5. Delete\n6. Exit\n>: ")

    if sel == '1':
        sp.call('cls', shell=True)
        id__ = int(input("Id: "))
        roll = input("Roll: ")
        name = input("Name: ")
        phone = input("Phone: ")
        add_data(id__, roll, name, phone)

        #input("\n\nPress enter to back: ")

    elif sel == '2':
        sp.call('cls', shell=True)
        show_data()
        input("\n\nPress enter to back: ")

    elif sel == '3':
        sp.call('cls', shell=True)
        id_ = int(input("Enter ID: "))
        show_data_by_id(id_)      

        print("\n\nPress enter to back: ")

    elif sel == '4':
        sp.call('cls', shell=True)
        id__ = int(input("Enter ID: "))
        show_data_by_id(id__)

        print("\n")

        name = input("Name: ")
        phone = input("Phone: ")
        update_student(id__, name, phone)

        input("\n\nYour data has been updated\nPress enter to back: ")

    elif sel == '5':
        sp.call('cls', shell=True)
        id__ = int(input("Enter ID: "))
        show_data_by_id(id__)
        delete_student(id__)

        print("\n")
        input("\n\nYour data has been deleted\nPress enter to back: ")
    else:
        return 0
    return 1


while select():
    pass
#!usr/bin/env python3

class Empleado:
    # numero_empleados es una variable de la clase, al ser
    # modificada se modifica para toda la clase.
    numero_empleados = 0

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        # Se modifica el numero de empleados que hay globalmente
        Empleado.numero_empleados += 1

if __name__ == '__main__':
    # Aun no hay empleados
    print(Empleado.numero_empleados)
    emp1 = Empleado('Jose', 'Perez')
    emp2 = Empleado('Juan', 'Lopez')
    # Hay dos empleados
    print(Empleado.numero_empleados)

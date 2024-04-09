class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad


class empleado(Persona):
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)
        self.sueldo = sueldo


empleado1 = empleado("pablo", 22, 34222)
print(f'''
Empleado: {empleado1.nombre}
Edad: {empleado1.edad}
sueldo: {empleado1.sueldo}
''')

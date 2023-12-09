class Persona:
    def __init__(self, nombre, apellidos, edad, sexo, direccion, email, sueldo=0):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad
        self.sexo = sexo
        self.direccion = direccion
        self.email = email
        self.sueldo = sueldo

    def asignar_sueldo(self, sueldo):
        self.sueldo = sueldo

    def calcular_afp(self):
        afp = self.sueldo * 0.0287
        return afp

    def calcular_sfs(self):
        sfs = self.sueldo * 0.0304
        return sfs

    def calcular_irs(self):
        
        if self.sueldo <= 416220:
            irs = 0
        elif self.sueldo <= 624329:
            irs = (self.sueldo - 416220) * 0.15
        else:
            irs = (208107 * 0.15) + ((self.sueldo - 624329) * 0.20)

        return irs

    def imprimir_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Apellidos: {self.apellidos}")
        print(f"Edad: {self.edad}")
        print(f"Sexo: {self.sexo}")
        print(f"Dirección: {self.direccion}")
        print(f"Email: {self.email}")
        print(f"Sueldo: {self.sueldo}")
        print(f"AFP: {self.calcular_afp()}")
        print(f"SFS: {self.calcular_sfs()}")
        print(f"IRS: {self.calcular_irs()}")

persona1 = Persona("Juan", "Perez", 30, "M", "Calle 123", "juan@example.com", 50000)
persona1.imprimir_informacion()

#!/usr/bin/python3
from empleado import Empleado
class EmpleadoPermanente(Empleado):
    def __init__(self, nombre, apellido, dni, salario, antiguedad):
        super().__init__(nombre, apellido, dni, salario)
        self.antiguedad = antiguedad

    def calcular_comision(self):
        comision = self.salario * self.antiguedad / 100
        return comision

    def calcular_ingreso_total(self):
        mensaje = super().calcular_ingreso_total()
        return mensaje

    def coincide(self, texto_a_buscar):
        mensaje = super().coincide()
        return mensaje

    def mostrar_datos(self):
        texto = super().mostrar_datos()
        texto += f"Antigüedad: {self.antiguedad}\n"
        return texto

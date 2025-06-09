#Se tiene una lista de los alumnos de un curso, de los que se sabe nombre, apellido y legajo.
#Por otro lado se tienen las notas de los diferentes parciales que rindió cada uno de ellos con
#la siguiente información: materia que rindió, nota obtenida y fecha de parcial. Desarrollar un
#algoritmo que permita realizar la siguientes actividades:
##a. mostrar los alumnos ordenados alfabéticamente por apellido;
#b. indicar los alumnos que no desaprobaron ningún parcial;
#c. determinar los alumnos que tienen promedio mayor a 8,89;
#d. mostrar toda la información de los alumnos cuyos apellidos comienzan con L;
#e. mostrar el promedio de cada uno de los alumnos;
#f. mostrar todos los alumnos que rindieron la cátedra “Algoritmos y estructuras de datos”;
#g. indicar el porcentaje de parciales aprobados de un alumno indicado por el usuario;
#h. indicar cuantos alumnos aprobaron y desaprobaron parciales de la cátedra “Base de datos”;
#i. mostrar todos los alumnos que rindieron en el año 2020;
#j. debe modificar el TDA para implementar lista de lista.

from typing import Any, Optional
from clase_lista import List
from listaAlumnos import alumnos 

class Alumno:
    def __init__(self, nombre: str, apellido: str, legajo: int, parciales: list):
        self.nombre = nombre
        self.apellido = apellido
        self.legajo = legajo
        self.parciales = List()
        for p in parciales:
            # Convertir cada parcial en un objeto Parcial
            parcial_obj = Parcial(
                materia=p['materia'],
                nota=p['nota'],
                fecha=p['fecha']
            )
            self.parciales.append(parcial_obj)

    def __str__(self):
        return (self.nombre + " " + self.apellido + " - Legajo: " + str(self.legajo) )

class Parcial:
    def __init__(self, materia: str, nota: float, fecha: str):
        self.materia = materia
        self.nota = nota
        self.fecha = fecha

    def __str__(self):
        return (self.materia + " - Nota: " + str(self.nota) + " - Fecha: " + self.fecha)

def ordenar_por_apellido(item):
    return item.apellido
list_alumnos = List()
list_alumnos.add_criterion("apellido", ordenar_por_apellido)  # Agregar criterio de ordenación por apellido
for alumno in alumnos:
    # Convertir cada alumno en un objeto Alumno
    alumno_obj = Alumno(
        nombre=alumno['nombre'],
        apellido=alumno['apellido'],
        legajo=alumno['legajo'],
        parciales=alumno['parciales']
    )
    list_alumnos.append(alumno_obj)  # Agregar el objeto a la lista

# a. mostrar los alumnos ordenados alfabéticamente por apellido;

print("Alumnos ordenados alfabéticamente por apellido:")
list_alumnos.sort_by_criterion("apellido")
list_alumnos.show()  # Mostrar la lista de alumnos ordenados por apellido

#b. indicar los alumnos que no desaprobaron ningún parcial;
print("Alumnos que no desaprobaron ningún parcial:")
for alumno in list_alumnos:
    if all(parcial.nota >= 6 for parcial in alumno.parciales):
        print(alumno)

#c. determinar los alumnos que tienen promedio mayor a 8,89;
print("Alumnos con promedio mayor a 8,89:")
for alumno in list_alumnos:
    notas = [parcial.nota for parcial in alumno.parciales]
    if notas and sum(notas) / len(notas) > 8.89:
        print(alumno)

#d. mostrar toda la información de los alumnos cuyos apellidos comienzan con L;
print("Alumnos cuyos apellidos comienzan con L:")
for alumno in list_alumnos:
    if alumno.apellido.startswith('L'):
        print(alumno)
#e. mostrar el promedio de cada uno de los alumnos;
print("Promedio de cada alumno:")
for alumno in list_alumnos:
    notas = [parcial.nota for parcial in alumno.parciales]
    if notas:
        promedio = sum(notas) / len(notas)
        print(alumno.nombre, alumno.apellido, "Promedio:", promedio)
    else:
        print(alumno.nombre, alumno.apellido, "No tiene parciales")
#f. mostrar todos los alumnos que rindieron la cátedra “Algoritmos y estructuras de datos”;
print("Alumnos que rindieron 'Algoritmos y estructuras de datos':")
for alumno in list_alumnos:
    if any(parcial.materia == "Algoritmos y estructuras de datos" for parcial in alumno.parciales):
        print(alumno)
#g. indicar el porcentaje de parciales aprobados de un alumno indicado por el usuario;
def porcentaje_aprobados(alumno: Alumno) -> float:
    total_parciales = len(alumno.parciales)
    if total_parciales == 0:
        return 0.0
    aprobados = sum(1 for parcial in alumno.parciales if parcial.nota >= 6)
    return (aprobados / total_parciales) * 100
alumno_nombre = input("Ingrese el nombre del alumno para calcular el porcentaje de parciales aprobados: ")
alumno_apellido = input("Ingrese el apellido del alumno: ")
alumno_encontrado = None
for alumno in list_alumnos:
    if alumno.nombre == alumno_nombre and alumno.apellido == alumno_apellido:
        alumno_encontrado = alumno
        break
if alumno_encontrado:
    porcentaje = porcentaje_aprobados(alumno_encontrado)
    print(alumno_encontrado.nombre, alumno_encontrado.apellido, "Porcentaje de parciales aprobados:", porcentaje)
else:
    print("Alumno no encontrado")

#h. indicar cuantos alumnos aprobaron y desaprobaron parciales de la cátedra “Base de datos”;
def contar_aprobados_desaprobados(catedra: str) -> tuple:
    aprobados = 0
    desaprobados = 0
    for alumno in list_alumnos:
        for parcial in alumno.parciales:
            if parcial.materia == catedra:
                if parcial.nota >= 6:
                    aprobados += 1
                else:
                    desaprobados += 1
    return aprobados, desaprobados
aprobados_bd, desaprobados_bd = contar_aprobados_desaprobados("Base de datos")
print("Alumnos aprobados en 'Base de datos':", aprobados_bd)
print("Alumnos desaprobados en 'Base de datos':", desaprobados_bd)

#i. mostrar todos los alumnos que rindieron en el año 2020;
print("Alumnos que rindieron en el año 2020:")
for alumno in list_alumnos:
    if any(parcial.fecha.startswith('2020') for parcial in alumno.parciales):
        print(alumno)

﻿"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf
import time


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Encontrar buenos videos por categoría y país")
    print("3- Encontrar video tendencia por país")
    print("4- Encontrar video tendencia por categoría")
    print("5- Buscar los videos con más Likes")
    print("0- Salir")   
def SelectList():
    print("Seleccione el tipo de representación de la lista:")
    print("1- ARRAY_LIST")
    print("2- LINKED_LIST")
    inputs = input('Seleccione una opción para continuar \n')
    if int(inputs[0]) == 1:
        return "ARRAY_LIST"
    elif int(inputs[0]) == 2:
        return "LINKED_LIST"
    else:
        sys.exit(0)
def SelectAlgoritmo():
    print("Seleccione el tipo de algoritmo de ordenamiento iterativo:")
    print("1- selection")
    print("2- insertion")
    print("3- shell")
    print("4- merge")
    print("5- quick")
    inputs = input('Seleccione una opción para continuar \n')
    if int(inputs[0]) == 1:
        return 1
    elif int(inputs[0]) == 2:
        return 2
    elif int(inputs[0]) == 3:
        return 3
    elif int(inputs[0]) == 4:
        return 4
    elif int(inputs[0]) == 5:
        return 5
    else:
        sys.exit(0)
    
def initCatalog(TypeList):
    return controller.initCatalog(TypeList)

def loadData(catalog, TypeList):
    controller.loadData(catalog, TypeList)

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar \n')
    if int(inputs[0]) == 1:
        TypeList=SelectList()
        print("Cargando información de los archivos ....")
        catalog = initCatalog(TypeList)
        loadData(catalog, TypeList)
        print('videos cargados: ' + str(lt.size(catalog['videos'])))
        print('Canales cargados: ' + str(lt.size(catalog['channel'])))
        print('Categorias cargadas: ' + str(lt.size(catalog['category'])))

    elif int(inputs[0]) == 2:
        pass
    else:
        sys.exit(0)
sys.exit(0)

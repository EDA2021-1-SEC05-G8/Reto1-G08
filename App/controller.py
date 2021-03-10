"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de videos
def initCatalog(TypeList):
    """
    Llama la funcion de inicializacion del catalogo del modelo.
    """
    catalog = model.newCatalog(TypeList)
    return catalog


# Funciones para la carga de datos
def loadData(catalog, TypeList):
    loadVideos(catalog, TypeList)
    loadCategory(catalog)
    sortVideos(catalog)

def loadVideos(catalog, TypeList):
    videosfile = cf.data_dir + "videos-small.csv"
    input_file = csv.DictReader(open(videosfile, encoding='utf-8'))
    for video in input_file:
        model.addVideo(catalog, video, TypeList)
def loadCategory(catalog):
    categoryfile = cf.data_dir + "category-id.csv"
    input_file = csv.DictReader(open(categoryfile, encoding="utf-8"),  delimiter='\t')
    for category in input_file:
        model.addCategory(catalog, category)
# Funciones de ordenamiento
def sortVideos(catalog):
    """
    Ordena los libros por average_rating
    """
    return model.sortVideos(catalog)
# Funciones de consulta sobre el catálogo
def VidByCatPais(catalog, cat, pais, number):

    return model.VidByCatPais(catalog, cat, pais, number)

def VidByPais(catalog, pais):
    return model.VidByPais(catalog, pais)

def VidbyCat(catalog, cat):
    return model.VidbyCat(catalog, cat)

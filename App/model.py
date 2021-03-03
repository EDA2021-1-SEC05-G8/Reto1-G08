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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import selectionsort as sc
from DISClib.Algorithms.Sorting import insertionsort as ns
from DISClib.Algorithms.Sorting import mergesort as mg
from DISClib.Algorithms.Sorting import quicksort as qc
assert cf
import time

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def newCatalog(TypeList):
    catalog = {"videos": None,
                "channel":None,
                "category":None}
    catalog["videos"] = lt.newList()
    catalog["channel"] = lt.newList(TypeList, cmpfunction=comparechannel)
    catalog["category"] = lt.newList(TypeList, cmpfunction=comparecategory)
    return catalog

# Funciones para agregar informacion al catalogo
def addVideo(catalog, video, TypeList):
    lt.addLast(catalog['videos'], video)
    channels = video["channel_title"].split(",")
    for channel in channels:
        addChannel(catalog, channel.strip(), video, TypeList)
def addChannel(catalog, channelname, video, TypeList):
    channels = catalog["channel"]
    poschannel = lt.isPresent(channels, channelname)
    if poschannel > 0:
        channel = lt.getElement(channels, poschannel)
    else:
        channel = newChannel(channelname, TypeList)
        lt.addLast(channels, channel)
    lt.addLast(channel["videos"], video)
def addCategory(catalog, category):
    t = newCategory(category['name'], category['id'])
    lt.addLast(catalog["category"], t)
# Funciones para creacion de datos
def newChannel(name, TypeList):
    channel = {"name": "", "videos": None}
    channel["name"]=name
    channel["videos"]=lt.newList(TypeList)
    return channel
def newCategory(name, id):
    category = {"category_name": "", "category_id": ""}
    category["category_name"] = name
    category["category_id"]=id
    return category
# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista
def comparechannel(channelname1, channel):
    if (channelname1.lower() in channel["name"].lower()):
        return 0
    return -1
def comparecategory(name, id):
    return(name == id["name"])
def cmpVideosByViews(video1, video2):
     return (float(video1['views']) < float(video2['views']))

# Funciones de ordenamiento
def sortVideos(catalog, size, Algoritmo):
    sub_list = lt.subList(catalog['videos'], 1, size)
    sub_list = sub_list.copy()
    if Algoritmo ==1:
        print("111111")
        start_time = time.process_time()
        sorted_list = sc.sort(sub_list, cmpVideosByViews)
        stop_time = time.process_time()
        elapsed_time_mseg = (stop_time - start_time)*1000
    elif Algoritmo == 2:
        print("222222")
        start_time = time.process_time()
        sorted_list = ns.sort(sub_list, cmpVideosByViews)
        stop_time = time.process_time()
        elapsed_time_mseg = (stop_time - start_time)*1000
    elif Algoritmo == 3:
        print("333333")
        start_time = time.process_time()
        sorted_list = sa.sort(sub_list, cmpVideosByViews)
        stop_time = time.process_time()
        elapsed_time_mseg = (stop_time - start_time)*1000
    elif Algoritmo == 4:
        print("4444")
        start_time = time.process_time()
        sorted_list = mg.sort(sub_list, cmpVideosByViews)
        stop_time = time.process_time()
        elapsed_time_mseg = (stop_time - start_time)*1000
    elif Algoritmo == 5:
        print("55555")
        start_time = time.process_time()
        sorted_list = qc.sort(sub_list, cmpVideosByViews)
        stop_time = time.process_time()
        elapsed_time_mseg = (stop_time - start_time)*1000
    return elapsed_time_mseg

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
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def newCatalog():
    catalog = {"videos": None,
                "channel":None,
                "category":None}
    catalog["videos"] = lt.newList()
    catalog["channel"] = lt.newList("ARRAY_LIST", cmpfunction=comparechannel)
    catalog["category"] = lt.newList("ARRAY_LIST", cmpfunction=comparecategory)
    return catalog

# Funciones para agregar informacion al catalogo
def addVideo(catalog, video):
    lt.addLast(catalog['videos'], video)
    channels = video["channel_title"].split(",")
    for channel in channels:
        addChannel(catalog, channel.strip(), video)
def addChannel(catalog, channelname, video):
    channels = catalog["channel"]
    poschannel = lt.isPresent(channels, channelname)
    if poschannel > 0:
        channel = lt.getElement(channels, poschannel)
    else:
        channel = newChannel(channelname)
        lt.addLast(channels, channel)
    lt.addLast(channel["videos"], video)
def addCategory(catalog, category):
    t = 1
    lt.addLast(catalog["category"], t)
# Funciones para creacion de datos
def newChannel(name):
    channel = {"name": "", "videos": None}
    channel["name"]=name
    channel["videos"]=lt.newList("ARRAY_LIST")
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

# Funciones de ordenamiento
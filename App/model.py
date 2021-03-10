﻿"""
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
def VidByCatPais(catalog, cat, pais, number):
    videos = catalog["videos"]
    cmpcategoria = catalog["category"]
    bestvideos1 = lt.newList()
    bestvideos2 = lt.newList()
    idname=getVideosByCat(cmpcategoria, cat)
    i=1
    while i <= lt.size(videos):
        country = lt.getElement(videos, i).get("country")
        idvideo = lt.getElement(videos, i).get("category_id")
        if country == pais and idname == idvideo:
            
            video = lt.getElement(videos, i)
            lt.addLast(bestvideos1, video)
            print("unasfdd dsaavds ds")
        i=i+1
    for cont in range(1, number+1):
        video = lt.getElement(videos, cont)
        lt.addLast(bestvideos2, video)
        print("dfgsd fsdgs sfd")
    return bestvideos2

def VidByPais(catalog, pais):
    vidbypais = lt.newList()
    videos=catalog["videos"]
    i=1
    while i <= lt.size(videos):
        country = lt.getElement(videos, i).get("country")
        if country == pais:
            video = lt.getElement(videos, i)
            lt.addLast(vidbypais, video)
        i=i+1
    #   obtenemos los id dentro de una lista
    new_list=[]
    j=1
    while j <= lt.size(vidbypais):
        video_id=lt.getElement(vidbypais, j).get("video_id")
        new_list.append(video_id)
        j=j+1
    print(new_list)
    #   hacemos una lista con el numero de elementos de cada una
    countlista = [new_list.count(num) for num in new_list]
    # obtenemos el mayor elemeto y su indice
    max_num = max(countlista)
    print(max_num)
    max_index = countlista.index(max_num)
    max_id=new_list[max_index]
    print(max_id)
    # devolvemos el elemento
    k=1
    video_max1=lt.getElement(vidbypais, k)
    while k <= lt.size(vidbypais):
        video_max2=lt.getElement(vidbypais, k).get("video_id")
        if video_max2 == max_id:
            video_max1=lt.getElement(vidbypais, k)
            break
        k=k+1
    print(video_max1)
    return video_max1        

# Funciones utilizadas para comparar elementos dentro de una lista
def comparechannel(channelname1, channel):
    if (channelname1.lower() in channel["name"].lower()):
        return 0
    return -1
def comparecategory(name, id):
    return(name == id["name"])
def getVideosByCat(catalog, name):
    i=1
    idname="jaja"
    while i <= lt.size(catalog):
        categoria = lt.getElement(catalog, i).get("category_name")
        if str(categoria) == name:
            idname = lt.getElement(catalog, i).get("category_id")
            print(idname)
            break
        else:
            i=i+1
    return idname
def cmpVideosByViews(video1, video2):
     return (float(video1['views']) < float(video2['views']))

# Funciones de ordenamiento
def sortVideos(catalog):
    print("4444")
    mg.sort(catalog["videos"], cmpVideosByViews)

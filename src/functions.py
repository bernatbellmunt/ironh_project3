# importo llibreries
import pandas as pd
from pandas import json_normalize
import requests 
import json
import os
from dotenv import load_dotenv #conda install -c conda-forge python-dotenv
import time
import folium
from folium import Choropleth, Circle, Marker, Icon, Map
from folium.plugins import HeatMap, MarkerCluster
import os
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import numpy as np
from geopy.distance import geodesic as GD


load_dotenv()
key = os.getenv("4squarekey")

def get_query_coord(query,latitude,longitude):

    url = f"https://api.foursquare.com/v3/places/nearby?ll={latitude}%2C{longitude}&query={query}&limit=1"

    headers = {
        "accept": "application/json",
        "Authorization": f"{key}"}
    response = requests.get(url, headers=headers).json()
    newlist=[]
    for lista in response["results"]:
        lat= lista["geocodes"]["main"]["latitude"]
        long = lista["geocodes"]["main"]["longitude"]
        distance = lista["distance"]
        coord = [lat,long]
        newlist.append(coord)

    return newlist

def get_query_dist(query,latitude,longitude):

    url = f"https://api.foursquare.com/v3/places/nearby?ll={latitude}%2C{longitude}&query={query}&limit=1"

    headers = {
        "accept": "application/json",
        "Authorization": f"{key}"}
    response = requests.get(url, headers=headers).json()
    newlist=[]
    for lista in response["results"]:
        lat= lista["geocodes"]["main"]["latitude"]
        long = lista["geocodes"]["main"]["longitude"]
        distance = lista["distance"]
        newlist.append(distance)

    return newlist

def get_query_to_map(query,latitude,longitude):

    url = f"https://api.foursquare.com/v3/places/nearby?ll={latitude}%2C{longitude}&query={query}&limit=10"

    headers = {
        "accept": "application/json",
        "Authorization": f"{key}"}
    response = requests.get(url, headers=headers).json()
    newlist=[]
    for lista in response["results"]:
        lat= lista["geocodes"]["main"]["latitude"]
        long = lista["geocodes"]["main"]["longitude"]
        name = lista["name"]
        
        newlist.append({"name":name,"lat":lat,"long":long})
    
    df = pd.DataFrame(newlist)
    mapa = Map(location = [latitude,longitude], zoom_start=10)
    for index,row in df.iterrows():

        #primer iconi, depres marcador
        icono = {"location":[row["lat"],row["long"]]}

        marker = Marker(**icono)


        marker.add_to(mapa)

    return mapa


def get_coord_category(cat,latitude,longitude):

    url = f"https://api.foursquare.com/v3/places/nearby?ll={latitude}%2C{longitude}&categories={cat}"

    headers = {
        "accept": "application/json",
        "Authorization": f"{key}"}
    response = requests.get(url, headers=headers).json()
    newlist=[]
    for lista in response["results"]:
        lat= lista["geocodes"]["main"]["latitude"]
        long = lista["geocodes"]["main"]["longitude"]
        newlist.append([lat,long])
    
    return newlist

def get_dist_category(cat,latitude,longitude):

    url = f"https://api.foursquare.com/v3/places/nearby?ll={latitude}%2C{longitude}&categories={cat}"

    headers = {
        "accept": "application/json",
        "Authorization": f"{key}"}
    response = requests.get(url, headers=headers).json()
    newlist=[]
    for lista in response["results"]:
        lat= lista["geocodes"]["main"]["latitude"]
        long = lista["geocodes"]["main"]["longitude"]
        distance = lista["distance"]
        newlist.append(distance)
    return newlist

def get_avg_distance (list_coord, reference):
    distances =[]
    for coord in list_coord:

        distances.append(GD(coord, reference).km)
    avg_distance = sum(distances)/len(distances)
    return avg_distance



#defineixo funció que em tornara un json del filtre que li passo
def plot_category(cat,latitude,longitude):

    url = f"https://api.foursquare.com/v3/places/nearby?ll={latitude}%2C{longitude}&categories={cat}"

    headers = {
        "accept": "application/json",
        "Authorization": f"{key}"}
    response = requests.get(url, headers=headers).json()
    newlist=[]
    for lista in response["results"]:
        lat= lista["geocodes"]["main"]["latitude"]
        long = lista["geocodes"]["main"]["longitude"]
        name = lista["name"]
        
        newlist.append({"name":name,"lat":lat,"long":long})
    
    df = pd.DataFrame(newlist)
    mapa = Map(location = [latitude,longitude], zoom_start=15)
    for index,row in df.iterrows():

        #primer iconi, depres marcador
        icono = {"location":[row["lat"],row["long"]]}

        marker = Marker(**icono)


        marker.add_to(mapa)

    return mapa 

    

def clean_coord(list_):
    clean_coord=[]
    for i in range(len(list_)):
        if list_[i]==[]:
            clean_coord.append(np.nan)
        else:
            clean_coord.append(list_[i][0])
    return clean_coord


def get_avg_distance_from_list (list_dist):
    avg_distance_list =[]
    for dist in list_dist:
        avg_distance = sum(dist)/len(dist)
        avg_distance_list.append(avg_distance)
    return avg_distance_list

def get_multiquery_dist(query,latitude,longitude):

    url = f"https://api.foursquare.com/v3/places/nearby?ll={latitude}%2C{longitude}&query={query}"

    headers = {
        "accept": "application/json",
        "Authorization": f"{key}"}
    response = requests.get(url, headers=headers).json()
    newlist=[]
    for lista in response["results"]:
        distance = lista["distance"]
        newlist.append(distance)

    return newlist

def scrape_table(url, table, class_):
    '''This function receives a string url, the table "class"
    and the class of that table. 
    It returns a dataframe for the table in that url'''
    
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find(table, {'class':class_}).tbody
    rows = table.find_all('tr')
    rows = list(rows)
    rows = [list(row) for row in rows]
    df_url = pd.DataFrame(rows).astype(str)
    
    return df_url
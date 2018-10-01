#
# CS 196 Data Hackerspace
# Assignment 1: Data Parsing and NumPy
# Due September 24th, 2018
#

import json
import csv
import numpy as np

def histogram_times(filename):
    data1 = open(filename)
    data = csv.reader(data1)
    hours = []
    for time in data:
        if time[1] != '' and len(time[1]) == 5:
            hour = int(time[1][:2])
            hours.append(hour)
    
    data1.close()
    hist,bins = np.histogram(hours, bins=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24])
    return hist

def weigh_pokemons(filename, weight):
    with open(filename) as json_file:
        json_data = json.load(json_file)
        pokemon = []
        for i in range(0,len(json_data['pokemon'])):
            if float(json_data['pokemon'][i]['weight'][:-3]) == weight:
                pokemon.append(json_data['pokemon'][i]['name'])
                
        return pokemon
        
def single_type_candy_count(filename):
    with open(filename) as json_file:
        json_data = json.load(json_file)
        counter = 0
        for i in range(0,len(json_data['pokemon'])):
            if 'candy_count' in json_data['pokemon'][i] and len(json_data['pokemon'][i]['type'])==1:
                counter += json_data['pokemon'][i]['candy_count']
                
        return counter

def reflections_and_projections(points):
    import math
    
    newPoints = []
    for point in points:
        x = point[0]
        y = point[1]
        reflectY = 2 - y
        rotateX = -reflectY
        rotateY = x
        projX = (rotateX/10) + (3*rotateY/10)
        projY = (3*rotateX/10) + (9*rotateY/10)
        newPoints.append([projX, projY])
        
    return np.array(newPoints)
        
        

def normalize(image):
    min = np.amin(image)
    max = np.amax(image)
    multiplier = 255/(max-min)
    
    newImage = np.empty((32,32))
    for i in range(0,32):
        for j in range(0,32):
            newImage[i][j] = multiplier*(image[i][j]-min)
        
    return newImage

def sigmoid_normalize(image):
    pass




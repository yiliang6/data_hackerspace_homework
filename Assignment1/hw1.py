# -*- coding: utf-8 -*-

#ALBERT LI
# CS 196 Data Hackerspace
# Assignment 1: Data Parsing and NumPy
# Due September 24th, 2018
#

import json
import requests
import csv
import numpy as np

def histogram_times(airplane_crashes):

    hours = [0 for i in range(24)]
    with open(airplane_crashes) as f:
        reader = csv.reader(f)
        my_list = list(reader)
    for i in range(len(my_list)):
        try:
            int(my_list[i][1][:2])
        except ValueError:
            continue
        hours[int(my_list[i][1][:2])] += 1
    print(hours)
    return hours

def weigh_pokemons(file, weight):
    with open(file) as f:
        pokedex = json.load(f)
        same_weight = list()
    for i in range(len(pokedex['pokemon'])):
        if (weight == float(pokedex['pokemon'][i]['weight'].split(" ")[0])):
            same_weight.append(pokedex['pokemon'][i]['name'])
    print(same_weight)
    return same_weight

def single_type_candy_count(filename):
    with open(filename) as f:
        file = json.load(f)
    count = 0
    for pokemon in file['pokemon']:
        if 'candy_count' in pokemon and len(pokemon['type']) == 1:
            count += pokemon['candy_count']
    return count

def reflections_and_projections(points):
    arr = np.array(points)
    for i in range(len(arr[0])):
        arr[1][i] = 2 - 1 * arr[1][i]
    rotate_90 = [[0, -1], [1, 0]]
    rotation = np.matmul(rotate_90, arr)
    project_points = [[0.1, 0.3], [0.3, 0.9]]
    projection = np.matmul(project_points, rotation)
    return projection

def normalize(image):
    normalization = image
    minimum = norm_image.min()
    maximum = norm_image.max()
    if minimum == maximum:
        return normalization
    else:
        normalization = (255 * (normalization - minimum) / (maximum - minimum))
    return normalization

def sigmoid_normalize(image):
    p = image
    if (normalization == 0):
        return p
    #for i in range(0, len(num)):
    p = float(255.0 / (1 + np.e ** ((norm_image - 128) / -a)))
    normalization = p
    return normalization

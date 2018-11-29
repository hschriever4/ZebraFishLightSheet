#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 14:07:40 2018

@author: hschriever
"""

import cv2
import glob
from skimage import io
from pims import ImageSequence
import numpy as np
import matplotlib.pyplot as plt

name = '/Users/jbransonbyers/Downloads/img_align_celeba'

def imagesToRows(rawData):
    print("Converting data for PCA compatibility...")
    #Takes a numpy array as input
    #Need to make sure which dimension the images are stored in
    
    size            = rawData.shape
    numImages       = size[1]
    dataPcaFormat   = np.zeros((size[1],size[2]*size[3]))
    print('There are ' + str(len(rawData)) + ' images.')
    
    for n in range(numImages):
        dataPcaFormat[n] = np.ndarray.flatten(rawData[0][n])
        
    print('Done.')
    return dataPcaFormat

def vectorToImage(vector, imageShape):
    print('this does nothing')
#this function not currently used in script

def createDataMatrix(images):
    print("Creating data matrix",end=" ... ")
    ''' 
    Allocate space for all images in one data matrix. 
        The size of the data matrix is
        ( w  * h  * 3, numImages )
        
        where,
         
        w = width of an image in the dataset.
        h = height of an image in the dataset.
        3 is for the 3 color channels.
        '''
   
    numImages = len(images)
    sz = images[0].shape
    data = np.zeros((numImages, sz[0] * sz[1] * sz[2]), dtype=np.float32)
    for i in range(0, numImages):
        image = images[i].flatten()
        data[i,:] = image
     
    print("DONE")
    return data

'''

function to save the eigan images under the correct name

'''
def NameFile(path):
    
    file_name = ''
    
    for i in range(len(path)):
        
        if path[-(i+1)] != '/':
            file_name = path[-i] + file_name
            
        if path[-(i+1)] == '/':
            break
    
    return file_name[:len(file_name)-4]


'''

function to print and save eigan images
takes 4 arguments
1. array containing eigan images
2. number of eigen vectors
3. dirrectory name of the video the code is analyzing
4. name you want to save the file as

'''

def print_and_save(arr, num, path, name):

    fig = plt.figure(figsize=(8, 8))

    for i in range(num):
    
        img = arr[i]
        fig.add_subplot(1, num, i+1)
        plt.imshow(img, cmap = 'gray')
        plt.xlabel('negative eigen image\n' + str(i+1) + ' of ' + str(num), fontsize=10)

    plt.savefig(name + NameFile(path), dpi = 600)
    plt.show()



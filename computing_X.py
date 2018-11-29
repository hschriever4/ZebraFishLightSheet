#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 13:54:14 2018

@author: hschriever
"""
import numpy as np
from skimage import io
import cv2
import matplotlib.pyplot as plt

#input from command line
path = input('what is the path?\n')

'''

***   Creating X   ***

'''

# IMPORT DATA HERE
tif = io.imread(path)

# storing the tiff in the numpy array named N
N = np.array(tif)
print(N.shape)


'''
assigning names to the dimensions of N
N is a 3D numpy array
the shape of N is (depth, rows, columns)
where depth is the number of frames in the video (slices in the stack)
rows is the heigth of a frame
columns is the width of a frame

'''
depth = N.shape[0]
rows = N.shape[1]
columns = N.shape[2]


'''
making the shape of the matrix X
X is a 2D numpy array
X has (depth of N) columns
X has (rows of N * columns of N) rows

'''
X_shape = [(rows * columns) , depth]


# creating X with the correct shape filled with zeros
X = np.zeros(X_shape)

i = 0
j = 0

'''
Assigning the correct values to X from N
restructureing the data from N into X
the value of X at (i,j) is equal to the value of N at (z,x,y) where
j = z and i = x + (y * rows)

'''
for z in range(depth):
    
    j = z
    
    for y in range(columns):
        for x in range(rows):
            
            i = x + (y * rows)
            
            X[i][j] = N[z][x][y]

'''

***   SVD   ***

'''

running = True

#create a random matrix for testing
#a = np.random.rand(134208, 409)

A = np.transpose(X)

image_size = (rows, columns)

#This version of PCA requires each image to be stored in a row
mean, eigen_vectors = cv2.PCACompute (A, mean = None, maxComponents = 1)

eigen_Images = []

#take the eignevectors and make them into eigenimages
for eigen_vector in eigen_vectors:
    eigenImage = eigen_vector.reshape(image_size)
    eigen_Images.append(eigenImage)
    
plt.imshow(eigen_Images[0])

print('done')
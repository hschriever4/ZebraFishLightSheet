#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 13:51:13 2018

@author: hschriever
"""

import numpy as np
import cv2
from pims import ImageSequence

#Import the data and convert to np array
#input from command line
DIR_NAME = input('what is the path?\n')

NUM_EIGENVECTORS    = 3

raw_data            = np.array(ImageSequence(DIR_NAME))
size                = raw_data.shape
image_size          = (size[2],size[3])
data_PCA_format     = imagesToRows(raw_data) #depth assumed to be in dim 2

mean, eigen_vectors = cv2.PCACompute (data_PCA_format, mean = None, maxComponents = NUM_EIGENVECTORS)

#initializing lists that will contain the eigan images
eigen_images        = []
eigen_images_pos    = []
eigen_images_neg    = []


'''

Creating the eigan images

eigen_images is a list of the complete eigan images
eigen_images_pos is a list of the positive eigan images
eigen_images_neg is a list of the negative eigan images multiplied by -1

'''
for eigen_vector in eigen_vectors:
    
    eigen_image = eigen_vector.reshape(image_size)
    
    eigen_image_pos_mask = eigen_image >= 0
    eigen_image_neg_mask = eigen_image <= 0
    
    eigen_image_pos = eigen_image * eigen_image_pos_mask
    eigen_image_neg = (eigen_image * eigen_image_neg_mask) * -1
    
    eigen_images.append(eigen_image)
    eigen_images_pos.append(eigen_image_pos)
    eigen_images_neg.append(eigen_image_neg)


'''

Printing and Saving the Eigan Images

'''

'''
#printing and saving complete eigan images
print_and_save(eigen_images, NUM_EIGENVECTORS, DIR_NAME, 'eigan_image_complete_')

#printing and saving positive eigan images
print_and_save(eigen_images_pos, NUM_EIGENVECTORS, DIR_NAME, 'eigan_image_positive_')

#printing and saving negative eigan images
print_and_save(eigen_images_neg, NUM_EIGENVECTORS, DIR_NAME, 'eigan_image_negative_')
'''

#creating the mask to mask the video
mask = create_mask(eigen_images)

MASK = np.empty(shape = data_PCA_format.size)
print (MASK)

'''
for i in range(data_PCA_format.size[0]):
    MASK[:i] = mask
    
'''

print (data_PCA_format.shape)
print(mask.flatten('F').shape)



'''
movie = raw_data
depth = size[1]
rows = size[2]
columns= size[3]

for z in range(depth):
    for x in range(rows):
        for y in range(columns):
            
            if mask[x][y] == False:
                movie[0][z][x][y] = 0
                
    
'''
print("Script passes tests.")



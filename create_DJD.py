#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 14:49:20 2020

@author: sampatghosh
"""

from os import listdir
import numpy as np
import pandas as pd
from PIL import Image
import matplotlib.pyplot as plt

actions_label = ['',
                 'high-arm-wave',
                 'horizontal-arm-wave',
                 'hammer',
                 'hand-catch',
                 'forward-punch',
                 'high-throw',
                 'draw-x',
                 'draw-tick',
                 'draw-circle',
                 'hand-clap',
                 'two-hand-wave',
                 'side-boxing',
                 'bend',
                 'forward-kick',
                 'side-kick',
                 'jogging',
                 'tennis-swing',
                 'tennis-serve',
                 'golf-swing',
                 'pick-up-and-throw']    

def get_label(file):
    action = 0
    subject = 0
    subset = 0
    i = 1
    while file[i] != '_':
        action = action*10 + int(file[i])
        i += 1
    i += 2
    while file[i] != '_':
        subject = subject*10 + int(file[i])
        i += 1
    i += 2
    #while file[i] != '_':
        #subset = subset*10 + int(file[i])
        #i += 1
    return action,subject

def create_DJD(data_dir):
    print('Loading MSR 3D Data, data directory %s' % data_dir)
    points = [ 1,  8, 10, 12, 0,  7,  9, 11, 19,  2,  3,  6, 4, 13, 15, 17, 5, 14, 16, 18] # MSRAction3D
    #points = [ 4,  5,  6,  7,  8,  9, 10, 11,  0,  1,  2,  3, 16, 17, 18, 19, 12, 13, 14, 15] # UTD-MAD
    #points = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
    for file in sorted(listdir(data_dir)): # iterate through the files
        
        action = np.loadtxt(data_dir+'/'+file)[:, :3] # read file

        # resize to number aof frames X number of joints X coordinates
        action  = action.reshape((action.shape[0]//20, 20, 3))
        #print(action[0])

        #print(action.shape)
        R = []
        G = []
        B = []
        #R = np.asarray(np.uint8(R))
        #G = np.asarray(np.uint8(G))
        #B = np.asarray(np.uint8(B))
        # iterate through all the frames in the file
        for frame in action:
            #minimum = np.min(frame)
            #maximum = np.max(frame)
            
            #print(maximum,minimum)
            #print(frame)
            minX = min(frame[:,0])
            maxX = max(frame[:,0])
            
            minY = min(frame[:,1])
            maxY = max(frame[:,1])
            
            minZ = min(frame[:,2])
            maxZ = max(frame[:,2])
            for i in points:                         
                newX = (frame[i][0] - minX) / (maxX - minX)
                newY = (frame[i][1] - minY) / (maxY - minY)
                newZ = (frame[i][2] - minZ) / (maxZ - minZ)
                R.append(newX)
                G.append(newY)
                B.append(newZ)
        R = np.asarray(R).reshape(action.shape[0],20)  
        G = np.asarray(G).reshape(action.shape[0],20)
        B = np.asarray(B).reshape(action.shape[0],20)

        R = np.transpose(R)
        G = np.transpose(G)
        B = np.transpose(B)
        
        R = np.transpose(R)
        G = np.transpose(G)
        B = np.transpose(B)
        
        DJD = np.ndarray([action.shape[0],20,3])
        
        DJD[:,:,0] = R
        DJD[:,:,1] = G
        DJD[:,:,2] = B

        img = Image.fromarray(np.uint8(DJD*255))

        action,subject = get_label(file)
        act = str(action)
        if action < 10:
        	act = '0'+str(action)

        if subject % 2 == 0:
            img.save('/home/sampatghosh/MajorProject/NUCLA_DJD/subject_even/'+file[:-4]+'.jpg')
        else:
            img.save('/home/sampatghosh/MajorProject/NUCLA_DJD/subject_odd/'+file[:-4]+'.jpg')
        #break


basePath = 'Data/MSRAction3DSkeleton'
# basePath = 'UTD_TXT/'
create_DJD(basePath)

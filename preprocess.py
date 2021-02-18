#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created By  : Jay Shah
# Contact  : https://www.public.asu.edu/~jgshah1/
# =============================================================================
''' Module takes in NIFTI (.nii) files, registered to MNI152 template (shape: 182 x 218 x182)
    and performs 4 steps:
    1. converts nifti to numpy
    2. normalizes the data [(x-mean)/std]
    3. clips the outlier intensity values
    4. removes background signals from images (check README for more details on this)

    Needs to have brain_region.npy in the same folder as this file for step-4
    Usage: python3 preprocess.py choose_your_nii_folder/ folder_to_store_processed_files/ '''

# =============================================================================
# Imports
# =============================================================================
import numpy as np
import nibabel as nib
import os, sys, glob

def nifti_to_numpy(file):
    data = nib.load(file).get_fdata()[:181, :217, :181]
    return data

def normalization(scan):
    scan = (scan - np.mean(scan)) / np.std(scan)
    return scan

def clip(scan):
    return np.clip(scan, -1, 2.5)

def background_removal(data, temp, file, output_folder):

    if not os.path.exists(output_folder):
        os.mkdir(output_folder)

    new_data = data[:,:,:]

    stack = [(0, 0, 0), (180, 0, 0), (0, 216, 0), (180, 216, 0)]
    visited = set([(0, 0, 0), (180, 0, 0), (0, 216, 0), (180, 216, 0)])

    def valid(x, y, z):
        if x < 0 or x >= 181:
            return False
        if y < 0 or y >= 217:
            return False
        if z < 0 or z >= 181:
            return False
        return True

    while stack:
        x, y, z = stack.pop()
        for dx, dy, dz in [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]:
            new_x, new_y, new_z = x + dx, y + dy, z + dz
            if valid(new_x, new_y, new_z) and (new_x, new_y, new_z) not in visited \
            and data[new_x, new_y, new_z] < -0.6 and temp[new_x, new_y, new_z] < 0.8:
                visited.add((new_x, new_y, new_z))
                new_data[new_x, new_y, new_z] = -10
                stack.append((new_x, new_y, new_z))

    filename = str(file.split('/')[-1].split('.')[0])
    print("Processing:", filename)
    
    new_data = np.where(new_data==-10, -np.ones((181, 217, 181)), new_data).astype(np.float32)
    np.save(output_folder + filename, new_data)

if __name__ == "__main__":
    
    folder = str(sys.argv[1])
    out_folder = str(sys.argv[2])

    temp = np.load('brain_region.npy')

    for file in glob.glob(folder + '*.nii'):
        data = nifti_to_numpy(file)
        data = normalization(data)
        data = clip(data)
        background_removal(data, temp, file, out_folder)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created By  : Jay Shah
# Contact  : https://www.public.asu.edu/~jgshah1/
# =============================================================================
''' Module converts NIFTI(.nii) files to Numpy (.npy) format
    Usage: python3 nii_to_npy.py choose_your_nii_folder/ folder_to_store_npy_files/ '''

# =============================================================================
# Imports
# =============================================================================
import nibabel as nib
import numpy as np
import glob, os, sys

def nifti_to_numpy(file, input_folder, output_folder):

	if not os.path.exists(output_folder):
		os.mkdir(output_folder)

	filename = str(file.split('/')[-1].split('.')[0])
	print("Processing: ", filename)

	img = nib.load(file)
	img_arr = img.get_fdata()
	img_arr = np.squeeze(img_arr)
	# print(img_arr.shape)
	np.save(output_folder+filename, img_arr)

	# # to check npy file's shape to verify
	# print(np.load(output_folder+filename+'.npy').shape)

if __name__ == "__main__":
    
    in_folder = str(sys.argv[1])
    out_folder = str(sys.argv[2])

    for file in glob.glob(in_folder + '*.nii'):
        data = nifti_to_numpy(file, in_folder, out_folder)
    print("Numpy files saved to ", out_folder)

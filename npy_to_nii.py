#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created By  : Jay Shah
# Contact  : https://www.public.asu.edu/~jgshah1/
# =============================================================================
''' Module converts numpy files to NIFTI-format
    also converts DPMs generated to NIFTI-format of size [181 x 217 x181] 
    Usage: python3 npy_to_nii.py choose_your_npy_folder/ folder_to_store_nifti_files/ '''

# =============================================================================
# Imports
# =============================================================================
import nibabel as nib
import numpy as np
import glob, os, sys

def probability_to_risk(raw):
    x1, x2 = raw[0, :, :, :], raw[1, :, :, :]
    risk = np.exp(x2) / (np.exp(x1) + np.exp(x2))
    return risk

def upsample(heat):
    new_heat = np.zeros((46*4, 55*4, 46*4))
    for start_idx1 in range(4):
        for start_idx2 in range(4):
            for start_idx3 in range(4):
                new_heat[start_idx1::4, start_idx2::4, start_idx3::4] = heat
    return new_heat[:181, :217, :181]

def numpy_to_nifti(file, input_folder, output_folder):

	if not os.path.exists(output_folder):
		os.mkdir(output_folder)

	filename = str(file.split('/')[-1].split('.')[0])
	print("Processing: ", filename)

	img = np.load(file)
	img = np.squeeze(img)

	# only if converting DPMs to NIFTI format
	# else comment it out
	img = upsample(probability_to_risk(img))

	new_image = nib.Nifti1Image(img, affine=np.eye(4))
	nib.save(new_image, out_folder+filename)


if __name__ == "__main__":
    
    in_folder = str(sys.argv[1])
    out_folder = str(sys.argv[2])

    for file in glob.glob(in_folder + '*.npy'):
        data = numpy_to_nifti(file, in_folder, out_folder)
    print("NIFTI files saved to ", out_folder)
        
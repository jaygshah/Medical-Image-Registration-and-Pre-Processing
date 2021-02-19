# Medical Image Registration and Pre-Processing
This module helps registering any size MRI scans to the standard MNI152 template with 1mm or 2mm resolutions.
And later on use the registered images to further pre-process in order to be able to use for deep learning models.

## Registration

Raw MRI scans are registered to the standard [MNI152](https://www.lead-dbs.org/about-the-mni-spaces/) template producing a 3-dimensional image of dimensions [182 x 218 x 182] and [91 x 109 x 91] in case of 1mm and 2mm resolutions respectively. The script uses FSL's flirt tool in order to do that.

### Usage

Takes in raw NIFTI files and produced registered NIFTI files with above mentioned dimensions.
```
for X in $(ls non_registered_nii_folder); 
do bash registration.sh non_registered_nii_folder/ $X $PWD/registered_nii_folder; done
```


## Pre-Process images

### Usage
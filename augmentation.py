# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 09:08:55 2023

@author: ahmad
"""

import cv2
import os
import imgaug.augmenters as iaa
import shutil


# You just need to specify the train dataset folder path:
train_folder = "" # Path to train dataset folder path

images_folder = os.path.join(train_folder, 'images')
labels_folder =  os.path.join(train_folder, 'labels')



def apply_augmentation(images_folder):
    
    dataset_folder = os.path.dirname(os.path.dirname(images_folder))
    augmented_images_folder = os.path.join(dataset_folder, "augmented_train", "images")
    
    os.makedirs(augmented_images_folder, exist_ok=True)
    
    for image_file in os.listdir(images_folder):
        image_path = os.path.join(images_folder, image_file)
        
        image = cv2.imread(image_path)
        
        # Define an augmentation sequence (including brightness, contrast, and hue adjustments)
        augmenter = iaa.Sequential([
            iaa.Multiply((0.5, 1.5)),  # Adjust brightness
            iaa.ContrastNormalization((0.5, 1.5)),  # Adjust contrast
            iaa.AddToHueAndSaturation((-30, 20))  # Adjust hue
        ])
        
        # Generate the augmented image
        augmented_image = augmenter.augment_image(image)
        
        # Save the augmented image with the same name as the original
        output_image_path = os.path.join(augmented_images_folder, image_file)
        cv2.imwrite(output_image_path, augmented_image)




def copy_labels(labels_folder):
    dataset_folder = os.path.dirname(os.path.dirname(labels_folder))
    copied_labels_folder = os.path.join(dataset_folder, "augmented_train", "labels")
    shutil.copytree(labels_folder, copied_labels_folder)
    print(f"Folder copied from {labels_folder} to {copied_labels_folder}")



apply_augmentation(images_folder)
copy_labels(labels_folder)

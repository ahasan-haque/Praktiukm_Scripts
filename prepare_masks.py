import json
import cv2
import os
import numpy as np

pixel_to_class_mapper = [{'class_id': 0, 'inst_id': 15}, {'class_id': 1, 'inst_id': 15}, {'class_id': 2, 'inst_id': 4}, {'class_id': 3, 'inst_id': 10}, {'class_id': 6, 'inst_id': 15}, {'class_id': 7, 'inst_id': 19}, {'class_id': 4, 'inst_id': 15}, {'class_id': 9, 'inst_id': 5}, {'class_id': 5, 'inst_id': 8}, {'class_id': 8, 'inst_id': 1}]

with open("gt_pose.json") as ground_truth, open("class_obj_taxonomy.json") as taxonomy:
    gt_dict = json.load(ground_truth)
    for key in gt_dict:
        value = gt_dict[key]
        file_path = f"mask/{key.zfill(6)}.png"
        mask_image = np.array(cv2.imread(file_path, cv2.IMREAD_GRAYSCALE))
        for unique_val in np.unique(mask_image):
            mask_image[mask_image != unique_val] = 0 
            mask_image[mask_image == unique_val] = 255
            # get file_name to save the file into the right directory
            target_gt = value[unique_val - 1]
            dir_id = str(target_gt["class_id"] + 1).zfill(2)
            dir_path = f"{dir_id}/mask"
            if not os.path.exists(dir_path):
                os.makedirs(dir_path)
             
            full_file_path = f"{dir_path}/{key.zfill(4)}.png"
            cv2.imwrite(full_file_path, mask_image)
            mask_image = np.array(cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)) 
             

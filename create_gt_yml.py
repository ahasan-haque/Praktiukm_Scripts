import json
import cv2
import os
import yaml
import numpy as np

with open("scene_camera.json") as f, open("gt_pose.json") as ground_truth:
    calibration_data = json.load(f)["pol"]
    gt_dict = json.load(ground_truth)
    cx = calibration_data["cx"] 
    cy = calibration_data["cy"] 
    fx = calibration_data["fx"] 
    fy = calibration_data["fy"]
    cam_K = [fx, 0.0, cx, 0.0, fy, cy, 0.0, 0.0, 1.0]
    phrase = ""
    for key in gt_dict:
        phrase += f"{key}:\n"
        phrase += "  cam_K: "
        phrase += f"{str(cam_K)}\n"
        phrase  += f"  depth_scale: 1.0\n"
    phrase.strip()
    for i in range(1, 11):
        with open(f"{str(i).zfill(2)}/info.yml", "w") as f:
            f.write(phrase)

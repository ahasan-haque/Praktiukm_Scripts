import os
import shutil


for i in range(1, 11):
    dest_dir_path = f"segnet_results/{str(i).zfill(2)}_label"
    source_dir_path = f"data/{str(i).zfill(2)}/mask"
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)
    for j in range(700):
        destination_file_path = f"{dest_dir_path}/{str(j).zfill(4)}_label.png"
        source_file_path = f"{source_dir_path}/{str(j).zfill(4)}.png"
        shutil.copy2(source_file_path, destination_file_path)

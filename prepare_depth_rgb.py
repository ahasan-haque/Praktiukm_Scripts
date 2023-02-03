import os
import shutil

# copy depth

for i in range(1, 11):
    index = str(i).zfill(2)
    print(f"Creating ../../tum_preprocessed/data/{index}")
    os.mkdir(f"../../tum_preprocessed/data/{index}")
    os.mkdir(f"../../tum_preprocessed/data/{index}/depth")
    for source in os.listdir("depth"):
        destination = source[2:]
        shutil.copy2(f"depth/{source}", f"../../tum_preprocessed/data/{index}/depth/{destination}") 

# copy rgb

for i in range(1, 11):
    index = str(i).zfill(2)
    print(f"Creating ../../tum_preprocessed/data/{index}")
    #os.mkdir(f"../../tum_preprocessed/data/{index}")
    os.mkdir(f"../../tum_preprocessed/data/{index}/rgb")
    for source in os.listdir("polarization"):
        destination = source[2:]
        shutil.copy2(f"polarization/{source}", f"../../tum_preprocessed/data/{index}/rgb/{destination}")   

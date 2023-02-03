import os
import random

for i in range(1, 11):
    index = str(i).zfill(2)
    file_paths = os.listdir(f"{index}/depth")
    file_paths = [path.split(".")[0] for path in file_paths]
    random.shuffle(file_paths)
    training_paths = file_paths[:550]
    test_paths = file_paths[550:]
    with open(f"{index}/train.txt", "w") as train_file, open(f"{index}/test.txt", "w") as test_file:
        train_file.write("\n".join(training_paths))
        test_file.write("\n".join(test_paths))  

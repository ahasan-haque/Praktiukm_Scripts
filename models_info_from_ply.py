import numpy as np

def parse_ply(file_path):
    with open(file_path, 'r') as file:
        data = file.readlines()
    
    start_index = data.index('end_header\n') + 1
    vertex_data = data[start_index:]
    # Convert the vertex data into a numpy array
    
    only_vertex_list = []
    for line in vertex_data:
        numbers = line.split()
        if len(numbers) == 3:
            only_vertex_list.append(line)
        else:
            break
     
    vertex_data = np.array([[float(i) for i in line.split()] for line in only_vertex_list])
    #print(vertex_data.shape)
    # Extract the minimum x, y, and z coordinates and compute the size in each dimension
    min_x = np.min(vertex_data[:, 0])
    min_y = np.min(vertex_data[:, 1])
    min_z = np.min(vertex_data[:, 2])
    size_x = np.max(vertex_data[:, 0]) - min_x
    size_y = np.max(vertex_data[:, 1]) - min_y
    size_z = np.max(vertex_data[:, 2]) - min_z

    # Compute the diameter as the maximum distance between any two points
    #diameter = np.max(np.sqrt(np.sum((vertex_data - np.mean(vertex_data, axis=1))**2, axis=1)))
    from scipy.spatial import distance
    diameter = np.max(distance.pdist(vertex_data[:, :3]))
    # Return the extracted information as a dictionary
    return {'diameter': diameter, 'min_x': min_x, 'min_y': min_y, 'min_z': min_z, 'size_x': size_x, 'size_y': size_y, 'size_z': size_z}

lst = []
with open("models_info.yml", "a+") as f:
    for i in range(1, 11):
        info = parse_ply(f'obj_{str(i).zfill(2)}.ply')
        lst.append(f"{i}: {info}\n")
        f.writelines(lst)


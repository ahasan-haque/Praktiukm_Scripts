import shutil

scales = {
    "1": [0.06418299999999999, 0.188347, 0.064361],
    "2": [0.07059, 0.144938, 0.06362999999999999],
    "3": [0.055162, 0.039412, 0.056001999999999996],
    "4": [0.112318, 0.073174, 0.085755],
    "5": [0.191841, 0.020562, 0.051271],
    "6": [0.191841, 0.020562, 0.051271],
    "7": [0.20804099999999998, 0.004982, 0.020811000000000003],
    "8": [0.045356999999999995, 0.134738, 0.046008],
    "9": [0.038946999999999996, 0.11944199999999999, 0.061759999999999995],
   "10": [0.230674, 0.0797, 0.094747]
}

for i in range(1, 11):
    source_file_name = f"obj_{str(i).zfill(2)}.ply"
    destination_list = []
    
    with open(source_file_name) as source, open("copy.ply", "a+") as destination:
        source_list = source.readlines()
        vertex_start_index = source_list.index('end_header\n') + 1
        destination_list.extend(source_list[:vertex_start_index])
        destination.writelines(destination_list)
        
        scaled_vertex_list = []
        index = vertex_start_index
        for line in source_list[vertex_start_index:]:
            numbers = [i.strip() for i in line.split()]
            if len(numbers) == 3:
               numbers[0] = float(numbers[0]) * scales["1"][0] 
               numbers[1] = float(numbers[1]) * scales["1"][2] 
               numbers[2] = float(numbers[2]) * scales["1"][2] 
               scaled_line = " ".join([str(n) for n in numbers]) + "\n"
               scaled_vertex_list.append(scaled_line)
               index += 1
            else:
               break
    
        destination.writelines(scaled_vertex_list)
        destination.writelines(source_list[index:]) 
    
    
    shutil.move("copy.ply", f"scaled_model/{source_file_name}")



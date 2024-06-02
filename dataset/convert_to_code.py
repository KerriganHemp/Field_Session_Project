import os

class_mapping = {
    'head': 0,
    'hips': 1,
    'front foot': 2,
    'back foot': 3,
    'front hand': 4,
    'back hand': 5
}

txt_dir = "C:\\Field_Session_Project\\dataset\\val\\labels"

for filename in os.listdir(txt_dir):
    if filename.endswith('.txt'):
        filepath = os.path.join(txt_dir, filename)
        
        with open(filepath, 'r') as file:
            lines = file.readlines()
        
        for i, line in enumerate(lines):
            for name in class_mapping:
                if str(name) in line:
                    new_line = line.replace(str(name), str(class_mapping[name]))
                    lines[i] = new_line
            
                
        
        # Write the modified contents back to the .txt file
        with open(filepath, 'w') as file:
            file.writelines(lines)  
    
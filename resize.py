import cv2
import os
import json

def resize_image(image_path, output_path, size=(608, 608)):
    image = cv2.imread(image_path)
    resized_image = cv2.resize(image, size)
    cv2.imwrite(output_path, resized_image)
    return image.shape[1], image.shape[0]
    
def resize_annotations(json_path, output_path, orig_size, new_size=(608, 608)):
    with open(json_path, 'r') as f:
        data = json.load(f)
    
    orig_width, orig_height = orig_size
    new_width, new_height = new_size
    
    scale_x = new_width / orig_width
    scale_y = new_height / orig_height

    for shape in data['shapes']:
        for point in shape['points']:
            point[0] *= scale_x
            point[1] *= scale_y
    
    data['imageWidth'] = new_width
    data['imageHeight'] = new_height
    
    with open(output_path, 'w') as f:
        json.dump(data, f, indent=4)
        

image_input_dir = "C:\\Field_Session_Project\\dataset\\train\\images"
image_output_dir = "C:\\Field_Session_Project\\resized_images"
json_input_dir = "C:\\Field_Session_Project\\annotated_swimmers"
json_output_dir = "C:\\Field_Session_Project\\resized_json"
new_size = (608, 608)

if not os.path.exists(image_output_dir):
    os.makedirs(image_output_dir)
if not os.path.exists(json_output_dir):
    os.makedirs(json_output_dir)
    
image_sizes = {}

for filename in os.listdir(image_input_dir):
    if filename.endswith('.jpg') or filename.endswith('.png'):
        image_input_path = os.path.join(image_input_dir, filename)
        image_output_path = os.path.join(image_output_dir, filename)
        
        # Resize image and get original size
        orig_size = resize_image(image_input_path, image_output_path, size=new_size)
        image_sizes[filename] = orig_size  # Store original size

        json_input_path = os.path.join(json_input_dir, os.path.splitext(filename)[0] + '.json')
        json_output_path = os.path.join(json_output_dir, os.path.splitext(filename)[0] + '.json')
        
        if os.path.exists(json_input_path):
            resize_annotations(json_input_path, json_output_path, orig_size, new_size=new_size)
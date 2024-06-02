


# import json
# import os

# def convert_polygon_to_bbox(polygon):
#     x_coordinates = [point[0] for point in polygon]
#     y_coordinates = [point[1] for point in polygon]
#     x_min = min(x_coordinates)
#     x_max = max(x_coordinates)
#     y_min = min(y_coordinates)
#     y_max = max(y_coordinates)
#     return x_min, y_min, x_max, y_max

# def normalize_bbox(x_min, y_min, x_max, y_max, image_width, image_height):
#     x_center = (x_min + x_max) / 2 / image_width
#     y_center = (y_min + y_max) / 2 / image_height
#     width = (x_max - x_min) / image_width
#     height = (y_max - y_min) / image_height
#     return x_center, y_center, width, height

# def convert_json_to_yolo(json_path, output_dir):
#     with open(json_path, 'r') as f:
#         data = json.load(f)
    
#     image_width = data['imageWidth']
#     image_height = data['imageHeight']
#     annotations = data['shapes']
    
#     yolo_annotations = []
#     for annotation in annotations:
#         label = annotation['label']
#         polygon = annotation['points']
        
#         x_min, y_min, x_max, y_max = convert_polygon_to_bbox(polygon)
#         x_center, y_center, width, height = normalize_bbox(x_min, y_min, x_max, y_max, image_width, image_height)
        
#         yolo_annotations.append(f"{label} {x_center:.6f} {y_center:.6f} {width:.6f} {height:.6f}")
    
#     output_filename = os.path.join(output_dir, os.path.splitext(os.path.basename(json_path))[0] + '.txt')
#     with open(output_filename, 'w') as f:
#         f.write('\n'.join(yolo_annotations))

# def batch_convert(json_dir, output_dir):
#     if not os.path.exists(output_dir):
#         os.makedirs(output_dir)
    
#     json_files = [f for f in os.listdir(json_dir) if f.endswith('.json')]
#     for json_file in json_files:
#         json_path = os.path.join(json_dir, json_file)
#         convert_json_to_yolo(json_path, output_dir)

# # Example usage
# json_dir = "C:\\Field_Session_Project\\annotated_swimmers"
# output_dir = "C:\\Field_Session_Project\\YOLO_files"

# batch_convert(json_dir, output_dir)

from ultralytics import YOLO
import cv2
import os

def pad_image_to_square(image, target_size):
    old_size = image.shape[:2]  # old_size is in (height, width) format
    ratio = float(target_size) / max(old_size)
    new_size = tuple([int(x * ratio) for x in old_size])
    
    image = cv2.resize(image, (new_size[1], new_size[0]))
    
    delta_w = target_size - new_size[1]
    delta_h = target_size - new_size[0]
    top, bottom = delta_h // 2, delta_h - (delta_h // 2)
    left, right = delta_w // 2, delta_w - (delta_w // 2)
    
    color = [0, 0, 0]
    new_image = cv2.copyMakeBorder(image, top, bottom, left, right, cv2.BORDER_CONSTANT, value=color)
    return new_image

def preprocess_images(image_dir, target_size):
    processed_dir = os.path.join(image_dir, 'processed')
    os.makedirs(processed_dir, exist_ok=True)
    
    for img_name in os.listdir(image_dir):
        img_path = os.path.join(image_dir, img_name)
        image = cv2.imread(img_path)
        if image is None:
            continue
        
        processed_image = pad_image_to_square(image, target_size)
        cv2.imwrite(os.path.join(processed_dir, img_name), processed_image)
        
path = 'YOLODataset_seg\\images\\train'
preprocess_images(path, 640)

model = YOLO('yolov8n-seg.pt')

model.train(
    data='dataset.yaml',
    epochs=50,
    imgsz=640,
    batch=32,
    name='swimmer-experiment',
    augment=True,
    lr0=0.001,
    patience=5,
    cache=True
)
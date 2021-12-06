import numpy as np
import cv2

def get_image_from_string_byte(image_data: str):
    jpg_as_np = np.frombuffer(image_data, dtype=np.uint8)
    img = cv2.imdecode(jpg_as_np, flags=1)

    return img

def resize_image(image, width: int, height: int):
    return cv2.resize(image, (width, height))

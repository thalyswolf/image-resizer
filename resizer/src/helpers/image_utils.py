import numpy as np
import cv2

from src.helpers.get_env import get_env

from src.core.entity.image_to_resize import ImageToResize

def get_image_from_string_byte(image_to_resize: ImageToResize):
    jpg_as_np = np.frombuffer(image_to_resize.image.str_data, dtype=np.uint8)
    img = cv2.imdecode(jpg_as_np, flags=1)
    return img

def resize_image(image, width: int, height: int):
    return cv2.resize(image, (width, height))

def save_img_resize_on_dir(image_resized, original_image: ImageToResize):
    directory = '{}{}.{}'.format(get_env('DEFAULT_STORAGE_DIR'), original_image._id, original_image.image.mime)
    print(directory)
    cv2.imwrite(directory, image_resized)

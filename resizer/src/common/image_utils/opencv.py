import numpy as np
import cv2

from src.helpers.get_env import get_env
from src.core.entity.image_to_resize import ImageToResize
from src.contract.image_utils_contract import ImageUtilsContract

class OpenCVImageUtils(ImageUtilsContract):
    
    @staticmethod
    def _get_image_from_string_byte(image_to_resize: ImageToResize):
        jpg_as_np = np.frombuffer(image_to_resize.image.str_data, dtype=np.uint8)
        img = cv2.imdecode(jpg_as_np, flags=1)
        return img

    @staticmethod
    def _resize_image(image, width: int, height: int):
        return cv2.resize(image, (width, height))

    def save_and_resize_image(self, original_image: ImageToResize):
        image = self._get_image_from_string_byte(original_image)
        image_resized = self._resize_image(image, original_image.new_height, original_image.new_width)

        directory = '{}{}.{}'.format(get_env('DEFAULT_STORAGE_DIR'), original_image._id, original_image.image.mime)
        cv2.imwrite(directory, image_resized)

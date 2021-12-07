from src.core.entity.image_to_resize import ImageToResize
from src.contract.image_utils_contract import ImageUtilsContract

class OpenCVImageUtilsTest(ImageUtilsContract):

    def save_and_resize_image(self, original_image: ImageToResize):
        print('saving...')

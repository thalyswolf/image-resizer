from typing import Dict

from src.helpers.image_utils import get_image_from_string_byte, resize_image
from src.contract.controller_contract import FilesRequest
import cv2

class ResizeImageUseCase:
    def __init__(self):
        pass

    def execute(self, request: Dict, file: FilesRequest):

        try:
            height = int(request['newHeight'])
            width = int(request['newWidth'])
        except:
            raise Exception()
        else:

            image_data = file.data
            image = get_image_from_string_byte(image_data)
            image_resized = resize_image(image, width, height)
       
            print('final')
            cv2.imwrite('./src/storage/teste-agora.{}'.format(file.mime), image_resized)
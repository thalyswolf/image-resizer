from typing import Dict

from src.helpers.image_utils import get_image_from_string_byte, resize_image, save_img_resize_on_dir
from src.contract.controller_contract import FilesRequest
from src.core.entity.image import Image
from src.core.entity.image_to_resize import ImageToResize
from src.contract.image_utils_contract import ImageUtilsContract
from src.helpers.handler_errors import InvalidWidthErrorException, InvalidHeightErrorException, InvalidTypeParamErrorException
class ResizeImageUseCase:

    def __init__(self, image_utils: ImageUtilsContract):
        self.image_utils = image_utils


    def execute(self, request: Dict, file: FilesRequest):

        if request.get('newHeight', None) is None:
            raise InvalidHeightErrorException()

        if request.get('newWidth', None) is None:
            raise InvalidWidthErrorException()

        try:

            image_object = Image()
            image_object.mime = file.mime
            image_object.str_data = file.data

            image_to_resize = ImageToResize()
            image_to_resize._id = request['_id']
            image_to_resize.new_height = int(request['newHeight'])
            image_to_resize.new_width = int(request['newWidth'])
            image_to_resize.image = image_object

        except:
            raise InvalidTypeParamErrorException()

        else:
            self.image_utils.save_and_resize_image(image_to_resize)

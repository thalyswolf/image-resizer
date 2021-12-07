from typing import Dict
from uuid import uuid4

from src.helpers.enum.accepted_images_format_enum import ACCEPTED_IMAGES_FORMAT
from src.helpers.get_env import get_env
from src.contract.messaging_queue_contract import MessagingQueueContract
from src.contract.controller_contract import FilesRequest
from src.core.entity.image import Image
from src.core.entity.image_to_resize import ImageToResize
from src.helpers.handler_errors import *

class ToQueueImageToResizeUseCase:

    def __init__(self, messaging_queue: MessagingQueueContract):
        self.messaging_queue = messaging_queue


    def execute(self, request: Dict, file: FilesRequest):
        
        if file.mime is None:
            raise InvalidFileMimeErrorException()

        if file.mime not in ACCEPTED_IMAGES_FORMAT:
            raise InvalidFileMimeErrorException()

        if file.data is None:
            raise InvalidFileDataErrorException()

        image = Image()
        image.mime = file.mime
        image.str_data = file.data

        image_to_resize = ImageToResize()
        image_to_resize._id = str(uuid4())
        image_to_resize.new_height = int(request.get('height', 0))
        image_to_resize.new_width = int(request.get('width', 0))
        image_to_resize.image = image

        if image_to_resize.new_height == 0:
            height = get_env('DEFAULT_TO_RESIZE_HEIGHT')
    
            if height is None:
                raise InvalidHeightErrorException()

            image_to_resize.new_height = int(height)


        if image_to_resize.new_width == 0:
            width = get_env('DEFAULT_TO_RESIZE_WIDTH')
    
            if width is None:
                raise InvalidWidthErrorException()

            image_to_resize.new_width = int(width)


        if image_to_resize.new_height < 0:
            raise InvalidHeightErrorException()

        if image_to_resize.new_width < 0 or image_to_resize.new_width is None:
            raise InvalidWidthErrorException()

        self.messaging_queue.send_to_resize(image_to_resize)

from typing import Dict
from src.contract.controller_contract import FilesRequest

from src.core.entity.image import Image


class ToQueueImageToResizeUseCase:
    def __init__(self, messaging_queue):
        self.messaging_queue = messaging_queue

    def execute(self, request: Dict, file: FilesRequest):

        image_to_resize = Image()
        image_to_resize.name = file.name
        image_to_resize.str_data = file.data

        self.messaging_queue.send_to_resize(image_to_resize)





        return {
            'message': 'Sucesso'
        }


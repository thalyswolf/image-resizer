from src.factory.get_image_utils_factory import get_image_utils_factory
from src.core.usecase.resize_image_usecase import ResizeImageUseCase
from src.contract.controller_contract import MessagingRequest, MessagingResponse


class ResizeImageController:

    @staticmethod
    def resize_image(request: MessagingRequest) -> MessagingResponse:
        try:
            image_utils = get_image_utils_factory()

            ResizeImageUseCase(image_utils).execute(request.payload, request.files[0])
        
        except Exception:
            from traceback import format_exc
            print(format_exc())

from src.core.usecase.resize_image_usecase import ResizeImageUseCase
from src.contract.controller_contract import MessagingRequest, MessagingResponse


class ResizeImageController:

    @staticmethod
    def resize_image(request: MessagingRequest) -> MessagingResponse:
        try:
            ResizeImageUseCase().execute(request.payload, request.files[0])
        
        except Exception:
            from traceback import format_exc
            print(format_exc())

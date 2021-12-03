from traceback import format_exc

from src.helpers.handler_errors import GenericErrorException
from src.core.usecase.to_queue_image_to_resize_usecase import ToQueueImageToResizeUseCase
from src.contract.controller_contract import HttpRequest, HttpResponse
from src.factory.messaging_queue_factory import get_queue_messaging_factory


class QueueImageToResizeController:

    @staticmethod
    def resize_image(request: HttpRequest) -> HttpResponse:
        try:
            messaging_queue = get_queue_messaging_factory()

            _ = ToQueueImageToResizeUseCase(messaging_queue).execute(request.payload, request.files[0])

            return HttpResponse(202, {
                'message': 'Accepted, but processing ...'
            })

        except Exception:
            return HttpResponse(500, {
                'message': format_exc()
            })


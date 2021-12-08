from traceback import format_exc

from src.helpers.enum.http_status_enum import HTTPResponseStatus
from src.helpers.handler_errors import *
from src.core.usecase.to_queue_image_to_resize_usecase import ToQueueImageToResizeUseCase
from src.contract.controller_contract import HttpRequest, HttpResponse
from src.factory.messaging_queue_factory import get_queue_messaging_factory


class QueueImageToResizeController:

    @staticmethod
    def resize_image(request: HttpRequest) -> HttpResponse:
        try:
            messaging_queue = get_queue_messaging_factory()

            _ = ToQueueImageToResizeUseCase(messaging_queue).execute(request.payload, request.files[0])

            return HttpResponse(HTTPResponseStatus.ACCEPTED_BUT_PROCESSING, {
                'message': 'Accepted!!! but processing ...'
            })

        except (InvalidHeightErrorException, InvalidWidthErrorException, InvalidFileMimeErrorException, InvalidFileMimeErrorException) as ie:
            return HttpResponse(HTTPResponseStatus.INVALID_DATA, {
                'message': ie.message
            })

        except GenericErrorException:
            return HttpResponse(HTTPResponseStatus.ERROR, {
                'message': 'Server internal error'
            })

        except Exception:
            return HttpResponse(HTTPResponseStatus.ERROR, {
                'message': format_exc()
            })

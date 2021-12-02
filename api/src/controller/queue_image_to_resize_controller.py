from src.core.usecase.to_queue_image_to_resize_usecase import ToQueueImageToResizeUseCase
from src.contract.controller_contract import HttpRequest, HttpResponse
from src.factory.messaging_queue_factory import get_queue_messaging_factory


class QueueImageToResizeController:

    def resize_image(self, request: HttpRequest) -> HttpResponse:
        messaging_queue = get_queue_messaging_factory()

        image = ToQueueImageToResizeUseCase(messaging_queue).execute(request.payload)

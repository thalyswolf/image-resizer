def resize_image():
    from src.controller.queue_image_to_resize_controller import QueueImageToResizeController
    from src.contract.controller_contract import HttpRequest

    http_request = HttpRequest(
        header={},
        payload={},
        params=None
    )

    controller = QueueImageToResizeController().resize_image(http_request)
    
print('aqui')
resize_image()
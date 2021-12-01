
class ToQueueImageToResizeUseCase:
    def __init__(self, messaging_queue):
        self.messaging_queue = messaging_queue

    def execute(self, image_request):
        self.messaging_queue.send_to_queue()

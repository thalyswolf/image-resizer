from src.adapter.image_to_resize_rabbitmq_adapter import image_to_resize_rabbitmq_adapter
from src.core.entity.image_to_resize import ImageToResize
from src.infra.queue.rabbitmq.connection import RabbitConnection
from src.contract.messaging_queue_contract import MessagingQueueContract

class RabbitMQMessaging(MessagingQueueContract):
    def send_to_resize(self, image_to_resize: ImageToResize):
        
        RabbitConnection().send_message(image_to_resize_rabbitmq_adapter(image_to_resize))
        print('The message was sent')

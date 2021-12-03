from src.infra.queue.rabbitmq.connection import RabbitConnection
from src.contract.messaging_queue_contract import MessagingQueueContract
from json import dumps

class RabbitMQMessaging(MessagingQueueContract):
    def send_to_resize(self, image):

        data = dumps({
            'message': 'teste hahahaha',
            'image': image.str_data
        })

        RabbitConnection().send_message(data)
        print('enviado')
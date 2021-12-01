from src.infra.queue.local.local import LocalMessaging
from src.infra.queue.rabbitmq.rabbitmq import RabbitMQMessaging

def get_queue_messaging_factory():
    return RabbitMQMessaging()
    return LocalMessaging()

from src.infra.queue.rabbitmq.rabbitmq import RabbitMQMessaging

def get_queue_messaging_factory():
    return RabbitMQMessaging()

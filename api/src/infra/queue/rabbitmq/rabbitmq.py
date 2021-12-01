from src.contract.messaging_queue_contract import MessagingQueueContract


class RabbitMQMessaging(MessagingQueueContract):
    def send_to_queue(self):
        print('send via rabbit')

        import pika

        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        channel = connection.channel()

        channel.queue_declare(queue='hello')

        channel.basic_publish(exchange='',
                            routing_key='hello',
                            body='Hello World!')

        print(" [x] Sent 'Hello World!'")

        connection.close()
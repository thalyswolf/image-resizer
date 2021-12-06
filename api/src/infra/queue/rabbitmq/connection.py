import pika
class RabbitConnection:
    
    _instance = None
    _connection = None

    # """ singleton pattern """
    # def __new__(cls):
    #     if cls._instance is None:
    #         cls._instance = object.__new__(cls)

    #     return cls._instance
    

    def __init__(self):
        if self._connection is None:
            self._connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
    
    def send_message(self, data: str):
        channel = self._connection.channel()
        channel.queue_declare(queue='images')

        channel.basic_publish(exchange='', routing_key='hello', body=data)

        


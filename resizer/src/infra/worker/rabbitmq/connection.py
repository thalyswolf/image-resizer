import pika
class RabbitConnection:
    
    _instance = None
    _connection = None

    def _do_connect(self, count=0):
        try:
            print('connecting {}'.format(count))
            self._connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
            print('connected')
        except:
            from time import sleep
            sleep(10)
            print('retrying ...')
            self._do_connect(count + 1)

    def __init__(self):
        if self._connection is None:
            self._do_connect()



    def listening_messages(self, callback_method):
        channel = self._connection.channel()
        channel.queue_declare(queue='hello')
        channel.basic_consume(queue='hello', on_message_callback=callback_method, auto_ack=True)

        print(' [*] Waiting for messages. To exit press CTRL+C')
        channel.start_consuming()

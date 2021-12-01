from src.contract.messaging_queue_contract import MessagingQueueContract


class LocalMessaging(MessagingQueueContract):
    def send_to_queue(self):
        print('send messaging')

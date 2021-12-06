from src.contract.messaging_queue_contract import MessagingQueueContract


class MockMessaging(MessagingQueueContract):
    def send_to_resize(self, image_to_resize):
        print('[mock] send messaging')

from abc import ABC, abstractmethod

class MessagingQueueContract(ABC):

    @abstractmethod
    def send_to_queue(self) -> None:
        pass
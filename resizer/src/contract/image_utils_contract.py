from abc import ABC, abstractmethod

from src.core.entity.image_to_resize import ImageToResize

class ImageUtilsContract(ABC):

    @abstractmethod
    def save_and_resize_image(self, original_image: ImageToResize) -> None:
        pass
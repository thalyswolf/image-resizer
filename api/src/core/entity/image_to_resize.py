from src.core.entity.image import Image


class ImageToResize:
    _id: str
    new_height: int
    new_width: int
    image: Image

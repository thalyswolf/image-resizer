from json import dumps

from src.core.entity.image_to_resize import ImageToResize

def image_to_resize_rabbitmq_adapter(image_resize: ImageToResize):
    return dumps({
        'body': {
            '_id': image_resize._id,
            'newWidth': image_resize.new_width,
            'newHeight': image_resize.new_height
        },
        'file': {
            'mime': image_resize.image.mime,
            'file': image_resize.image.str_data
        }
    })
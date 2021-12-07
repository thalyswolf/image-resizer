from json import loads
from src.adapter.rabbitmq_adapter import rabbitmq_adapter
from src.controller.resize_image_controller import ResizeImageController

from src.infra.worker.rabbitmq.connection import RabbitConnection


def send_to_controller(ch, method, properties, body):
    request = loads(body.decode("utf-8"))
    ResizeImageController.resize_image(rabbitmq_adapter(request))


def on_listening():
    try:
        RabbitConnection().listening_messages(send_to_controller)
    except:
        on_listening()

on_listening()
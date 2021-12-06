import pytest

from src.infra.queue.mock.mock import MockMessaging
from src.helpers.handler_errors import *
from src.core.usecase.to_queue_image_to_resize_usecase import ToQueueImageToResizeUseCase
from src.contract.controller_contract import FilesRequest


mock_messaging_queue = MockMessaging()

def test_should_raise_invalid_width_if_negative_value_on_to_queue_resize_image():

    with pytest.raises(InvalidWidthErrorException):
        ToQueueImageToResizeUseCase(mock_messaging_queue).execute({
            'width': -200,
            'height': 100
        }, FilesRequest('jpg', 'string'))

def test_should_raise_invalid_height_if_negative_value_on_to_queue_resize_image():

    with pytest.raises(InvalidHeightErrorException):
        ToQueueImageToResizeUseCase(mock_messaging_queue).execute({
            'width': 200,
            'height': -100
        }, FilesRequest('jpg', 'string'))

def test_should_raise_invalid_mime_type_value_on_to_queue_resize_image():

    with pytest.raises(InvalidFileMimeErrorException):
        ToQueueImageToResizeUseCase(mock_messaging_queue).execute({
            'width': 200,
            'height': 100
        }, FilesRequest('exe', 'string'))

def test_should_raise_null_mime_type_value_on_to_queue_resize_image():

    with pytest.raises(InvalidFileMimeErrorException):
        ToQueueImageToResizeUseCase(mock_messaging_queue).execute({
            'width': 200,
            'height': 100
        }, FilesRequest(None, 'string'))

def test_should_raise_null_file_data_value_on_to_queue_resize_image():

    with pytest.raises(InvalidFileDataErrorException):
        ToQueueImageToResizeUseCase(mock_messaging_queue).execute({
            'width': 200,
            'height': 100
        }, FilesRequest('jpg', None))

def test_should_return_sucess_to_queue_resize_image():

    ToQueueImageToResizeUseCase(mock_messaging_queue).execute({
        'width': 200,
        'height': 100
    }, FilesRequest('jpg', 'string'))

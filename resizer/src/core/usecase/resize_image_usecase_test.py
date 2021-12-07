import pytest
from uuid import uuid4
from faker import Faker

from src.contract.controller_contract import FilesRequest
from src.core.usecase.resize_image_usecase import ResizeImageUseCase
from src.common.image_utils.opencv_test import OpenCVImageUtilsTest
from src.helpers.handler_errors import *

faker = Faker()

def make_sut_file_request() -> FilesRequest:
    return FilesRequest(faker.word(), faker.word())

def make_sut_image_utils() -> OpenCVImageUtilsTest:
    return OpenCVImageUtilsTest()

def make_sut_request_sucess():
    sut_request = {
        '_id': faker.word(),
        'newHeight': faker.random_int(),
        'newWidth': faker.random_int()
    }
    return sut_request


def test_should_sucess():
    ResizeImageUseCase(make_sut_image_utils()).execute(make_sut_request_sucess(), make_sut_file_request())

def test_should_raise_invalid_width_if_new_width_is_null():
    sut_request = make_sut_request_sucess()
    sut_request['newWidth'] = None

    with pytest.raises(InvalidWidthErrorException):
        ResizeImageUseCase(make_sut_image_utils()).execute(sut_request, make_sut_file_request())

def test_should_raise_invalid_height_if_new_height_is_null():
    sut_request = make_sut_request_sucess()
    sut_request['newHeight'] = None

    with pytest.raises(InvalidHeightErrorException):
        ResizeImageUseCase(make_sut_image_utils()).execute(sut_request, make_sut_file_request())

def test_should_raise_invalid_height_if_new_height_is_not_informed():
    sut_request = {
        '_id': faker.word(),
        'newWidth': faker.random_int()
    }

    with pytest.raises(InvalidHeightErrorException):
        ResizeImageUseCase(make_sut_image_utils()).execute(sut_request, make_sut_file_request())


def test_should_raise_invalid_width_if_new_width_is_not_informed():
    sut_request = {
        '_id': faker.word(),
        'newHeight': faker.random_int()
    }

    with pytest.raises(InvalidWidthErrorException):
        ResizeImageUseCase(make_sut_image_utils()).execute(sut_request, make_sut_file_request())

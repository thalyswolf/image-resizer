from fastapi import FastAPI, File, Form, Response, Request, UploadFile

from src.adapter.fast_api_adapter import fast_api_adapter
from src.contract.controller_contract import FilesRequest
from src.controller.queue_image_to_resize_controller import QueueImageToResizeController


app = FastAPI()

@app.post('/resize-image')
def resize_image(file: UploadFile = File(...), height: str = Form(0), width: str = Form(0), response: Response = Response):

    request = {
        'body': {
            'height': int(height),
            'width': int(width)
        },
        'headers': None,
        'query': None,
        'files': [file]
    }

    result = QueueImageToResizeController.resize_image(fast_api_adapter(request))

    response.status_code = result.status_code

    return result.payload

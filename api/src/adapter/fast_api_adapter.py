from typing import Dict

from src.contract.controller_contract import HttpRequest, FilesRequest

def fast_api_adapter(request: Dict) -> HttpRequest:

    files = []

    for file in request['files']:
        files.append(FilesRequest(file.filename.split(".")[-1], str(file.file.read())))

    http_request = HttpRequest(
        header=request['headers'],
        payload=request['body'],
        params=request['query'],
        files=files
    )

    return http_request

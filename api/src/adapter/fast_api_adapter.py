from typing import Dict

from src.contract.controller_contract import HttpRequest, FilesRequest

def fast_api_adapter(request: Dict) -> HttpRequest:
    http_request = HttpRequest(
        header=request['headers'],
        payload=request['body'],
        params=request['query'],
        files=request['files']
    )

    return http_request

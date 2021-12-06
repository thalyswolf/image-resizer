from typing import Dict
import ast

from src.contract.controller_contract import MessagingRequest
from src.contract.controller_contract import FilesRequest

def rabbitmq_adapter(body: Dict) -> MessagingRequest:
    
    request = {
        'body': body['body'],
        'headers': None,
        'query': None,
        'files': [FilesRequest(body['file']['mime'], ast.literal_eval(body['file']['file']))]
        # 'files': [FilesRequest(body['file']['filename'], body['file']['file'])]

    }

    messaging_request = MessagingRequest(
        header=request['headers'],
        payload=request['body'],
        params=request['query'],
        files=request['files']
    )

    return messaging_request

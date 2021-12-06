from typing import List


class FilesRequest:
    name: str
    data: str

    def __init__(self, mime, data):
        self.mime = mime
        self.data = data


class HttpRequest:
    def __init__(self, header, payload, params, files:List[FilesRequest] = []):
        self.header = header
        self.payload = payload
        self.params = params
        self.files = files
        
    def __repr__(self):
        return (
            f"HttpRequest (header={self.header}, body={self.body}, query={self.query})"
        )

class HttpResponse:

    def __init__(self, status_code: int, body: any):
        self.status_code = status_code
        self.payload = body

    def __repr__(self):
        return f"HttpResponse (status_code={self.status_code}, body={self.body})"

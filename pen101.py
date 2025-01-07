#!/usr/bin/env python3
from mitmproxy import http
import json

class HTTPLogger:
    def __init__(self):
        self.data = []

    def log_request(self, flow: http.HTTPFlow):
        self.data.append({
            "type": "request",
            "method": flow.request.method,
            "url": flow.request.pretty_url,
            "headers": dict(flow.request.headers),
            "body": flow.request.text
        })

    def log_response(self, flow: http.HTTPFlow):
        self.data.append({
            "type": "response",
            "url": flow.request.pretty_url,
            "status_code": flow.response.status_code,
            "headers": dict(flow.response.headers),
            "body": flow.response.text
        })
        self.save_to_file()

    def save_to_file(self):
        with open("http_logs.json", "w") as file:
            json.dump(self.data, file, indent=4)



    def request(self, flow: http.HTTPFlow):
        self.log_request(flow)

    def response(self, flow: http.HTTPFlow):
        self.log_response(flow)


addons = [HTTPLogger()]

# -*- coding: utf-8 -*-

"""
    meraki_sdk

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""

class HttpResponse(object):

    """Information about an HTTP Response including its status code, returned
        headers, and raw body

    Attributes:
        status_code (int): The status code response from the server that
            corresponds to this response.
        headers (dict): A dictionary of headers (key : value) that were
            returned with the response
        raw_body (string): The Raw body of the HTTP Response as a string

    """

    def __init__(self,
                 status_code,
                 headers,
                 raw_body):
        """Constructor for the HttpResponse class

        Args:
            status_code (int): The response status code.
            headers (dict): The response headers.
            raw_body (string): The raw body from the server.

        """
        self.status_code = status_code
        self.headers = headers
        self.raw_body = raw_body

# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""

from meraki.api_helper import APIHelper
from meraki.configuration import Configuration
from meraki.controllers.base_controller import BaseController
from meraki.http.auth.custom_header_auth import CustomHeaderAuth

class EventsController(BaseController):

    """A Controller to access Endpoints in the meraki API."""


    def get_network_events(self,
                           options=dict()):
        """Does a GET request to /networks/{networkId}/events.

        List the events for the network

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    network_id -- string -- TODO: type description here.
                        Example: 
                    product_type -- string -- The product type to fetch events
                        for. This parameter is required for networks with
                        multiple device types. Valid types are wireless,
                        appliance, switch, systemsManager, and camera
                    included_event_types -- list of string -- A list of event
                        types. The returned events will be filtered to only
                        include events with these types.
                    excluded_event_types -- list of string -- A list of event
                        types. The returned events will be filtered to exclude
                        events with these types.
                    device_mac -- string -- The MAC address of the Meraki
                        device which the list of events will be filtered with
                    device_serial -- string -- The serial of the Meraki device
                        which the list of events will be filtered with
                    device_name -- string -- The name of the Meraki device
                        which the list of events will be filtered with
                    client_ip -- string -- The IP of the client which the list
                        of events will be filtered with. Only supported for
                        track-by-IP networks.
                    client_mac -- string -- The MAC address of the client
                        which the list of events will be filtered with. Only
                        supported for track-by-MAC networks.
                    client_name -- string -- The name, or partial name, of the
                        client which the list of events will be filtered with
                    sm_device_mac -- string -- The MAC address of the Systems
                        Manager device which the list of events will be
                        filtered with
                    sm_device_name -- string -- The name of the Systems
                        Manager device which the list of events will be
                        filtered with
                    per_page -- int -- The number of entries per page
                        returned. Acceptable range is 3 - 1000. Default is
                        10.
                    starting_after -- string -- A token used by the server to
                        indicate the start of the page. Often this is a
                        timestamp or an ID but it is not limited to those.
                        This parameter should not be defined by client
                        applications. The link for the first, last, prev, or
                        next page in the HTTP Link header should define it.
                    ending_before -- string -- A token used by the server to
                        indicate the end of the page. Often this is a
                        timestamp or an ID but it is not limited to those.
                        This parameter should not be defined by client
                        applications. The link for the first, last, prev, or
                        next page in the HTTP Link header should define it.

        Returns:
            mixed: Response from the API. Successful operation

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(network_id=options.get("network_id"))

        # Prepare query URL
        _url_path = '/networks/{networkId}/events'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'networkId': options.get('network_id', None)
        })
        _query_builder = Configuration.base_uri
        _query_builder += _url_path
        _query_parameters = {
            'productType': options.get('product_type', None),
            'includedEventTypes': options.get('included_event_types', None),
            'excludedEventTypes': options.get('excluded_event_types', None),
            'deviceMac': options.get('device_mac', None),
            'deviceSerial': options.get('device_serial', None),
            'deviceName': options.get('device_name', None),
            'clientIp': options.get('client_ip', None),
            'clientMac': options.get('client_mac', None),
            'clientName': options.get('client_name', None),
            'smDeviceMac': options.get('sm_device_mac', None),
            'smDeviceName': options.get('sm_device_name', None),
            'perPage': options.get('per_page', None),
            'startingAfter': options.get('starting_after', None),
            'endingBefore': options.get('ending_before', None)
        }
        _query_builder = APIHelper.append_url_with_query_parameters(_query_builder,
            _query_parameters, Configuration.array_serialization)
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.http_client.get(_query_url, headers=_headers)
        CustomHeaderAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body)

    def get_network_events_event_types(self,
                                       network_id):
        """Does a GET request to /networks/{networkId}/events/eventTypes.

        List the event type to human-readable description

        Args:
            network_id (string): TODO: type description here. Example: 

        Returns:
            mixed: Response from the API. Successful operation

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(network_id=network_id)

        # Prepare query URL
        _url_path = '/networks/{networkId}/events/eventTypes'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'networkId': network_id
        })
        _query_builder = Configuration.base_uri
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.http_client.get(_query_url, headers=_headers)
        CustomHeaderAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body)

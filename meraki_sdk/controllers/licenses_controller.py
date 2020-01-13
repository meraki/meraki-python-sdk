# -*- coding: utf-8 -*-

"""
    meraki_sdk

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""

from meraki_sdk.api_helper import APIHelper
from meraki_sdk.configuration import Configuration
from meraki_sdk.controllers.base_controller import BaseController
from meraki_sdk.http.auth.custom_header_auth import CustomHeaderAuth

class LicensesController(BaseController):

    """A Controller to access Endpoints in the meraki_sdk API."""


    def get_organization_licenses(self,
                                  options=dict()):
        """Does a GET request to /organizations/{organizationId}/licenses.

        List the licenses for an organization

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    organization_id -- string -- TODO: type description here.
                        Example: 
                    per_page -- int -- The number of entries per page
                        returned. Acceptable range is 3 - 1000. Default is
                        1000.
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
                    device_serial -- string -- Filter the licenses to those
                        assigned to a particular device
                    network_id -- string -- Filter the licenses to those
                        assigned in a particular network
                    state -- StateEnum -- Filter the licenses to those in a
                        particular state. Can be one of 'active', 'expired',
                        'expiring', 'unused', 'unusedActive' or
                        'recentlyQueued'

        Returns:
            mixed: Response from the API. Successful operation

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(organization_id=options.get("organization_id"))

        # Prepare query URL
        _url_path = '/organizations/{organizationId}/licenses'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'organizationId': options.get('organization_id', None)
        })
        _query_builder = Configuration.base_uri
        _query_builder += _url_path
        _query_parameters = {
            'perPage': options.get('per_page', None),
            'startingAfter': options.get('starting_after', None),
            'endingBefore': options.get('ending_before', None),
            'deviceSerial': options.get('device_serial', None),
            'networkId': options.get('network_id', None),
            'state': options.get('state', None)
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

    def assign_organization_licenses_seats(self,
                                           options=dict()):
        """Does a POST request to /organizations/{organizationId}/licenses/assignSeats.

        Assign SM seats to a network. This will increase the managed SM device
        limit of the network

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    organization_id -- string -- TODO: type description here.
                        Example: 
                    assign_organization_licenses_seats --
                        AssignOrganizationLicensesSeatsModel -- TODO: type
                        description here. Example: 

        Returns:
            mixed: Response from the API. Successful operation

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(organization_id=options.get("organization_id"),
                                 assign_organization_licenses_seats=options.get("assign_organization_licenses_seats"))

        # Prepare query URL
        _url_path = '/organizations/{organizationId}/licenses/assignSeats'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'organizationId': options.get('organization_id', None)
        })
        _query_builder = Configuration.base_uri
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'content-type': 'application/json; charset=utf-8'
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(options.get('assign_organization_licenses_seats')))
        CustomHeaderAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body)

    def move_organization_licenses(self,
                                   options=dict()):
        """Does a POST request to /organizations/{organizationId}/licenses/move.

        Move licenses to another organization. This will also move any devices
        that the licenses are assigned to

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    organization_id -- string -- TODO: type description here.
                        Example: 
                    move_organization_licenses --
                        MoveOrganizationLicensesModel -- TODO: type
                        description here. Example: 

        Returns:
            mixed: Response from the API. Successful operation

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(organization_id=options.get("organization_id"),
                                 move_organization_licenses=options.get("move_organization_licenses"))

        # Prepare query URL
        _url_path = '/organizations/{organizationId}/licenses/move'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'organizationId': options.get('organization_id', None)
        })
        _query_builder = Configuration.base_uri
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'content-type': 'application/json; charset=utf-8'
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(options.get('move_organization_licenses')))
        CustomHeaderAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body)

    def move_organization_licenses_seats(self,
                                         options=dict()):
        """Does a POST request to /organizations/{organizationId}/licenses/moveSeats.

        Move SM seats to another organization

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    organization_id -- string -- TODO: type description here.
                        Example: 
                    move_organization_licenses_seats --
                        MoveOrganizationLicensesSeatsModel -- TODO: type
                        description here. Example: 

        Returns:
            mixed: Response from the API. Successful operation

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(organization_id=options.get("organization_id"),
                                 move_organization_licenses_seats=options.get("move_organization_licenses_seats"))

        # Prepare query URL
        _url_path = '/organizations/{organizationId}/licenses/moveSeats'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'organizationId': options.get('organization_id', None)
        })
        _query_builder = Configuration.base_uri
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'content-type': 'application/json; charset=utf-8'
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(options.get('move_organization_licenses_seats')))
        CustomHeaderAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body)

    def renew_organization_licenses_seats(self,
                                          options=dict()):
        """Does a POST request to /organizations/{organizationId}/licenses/renewSeats.

        Renew SM seats of a license. This will extend the license expiration
        date of managed SM devices covered by this license

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    organization_id -- string -- TODO: type description here.
                        Example: 
                    renew_organization_licenses_seats --
                        RenewOrganizationLicensesSeatsModel -- TODO: type
                        description here. Example: 

        Returns:
            mixed: Response from the API. Successful operation

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(organization_id=options.get("organization_id"),
                                 renew_organization_licenses_seats=options.get("renew_organization_licenses_seats"))

        # Prepare query URL
        _url_path = '/organizations/{organizationId}/licenses/renewSeats'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'organizationId': options.get('organization_id', None)
        })
        _query_builder = Configuration.base_uri
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'content-type': 'application/json; charset=utf-8'
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(options.get('renew_organization_licenses_seats')))
        CustomHeaderAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body)

    def get_organization_license(self,
                                 options=dict()):
        """Does a GET request to /organizations/{organizationId}/licenses/{licenseId}.

        Display a license

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    organization_id -- string -- TODO: type description here.
                        Example: 
                    license_id -- string -- TODO: type description here.
                        Example: 

        Returns:
            mixed: Response from the API. Successful operation

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(organization_id=options.get("organization_id"),
                                 license_id=options.get("license_id"))

        # Prepare query URL
        _url_path = '/organizations/{organizationId}/licenses/{licenseId}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'organizationId': options.get('organization_id', None),
            'licenseId': options.get('license_id', None)
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

    def update_organization_license(self,
                                    options=dict()):
        """Does a PUT request to /organizations/{organizationId}/licenses/{licenseId}.

        Update a license

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    organization_id -- string -- TODO: type description here.
                        Example: 
                    license_id -- string -- TODO: type description here.
                        Example: 
                    update_organization_license --
                        UpdateOrganizationLicenseModel -- TODO: type
                        description here. Example: 

        Returns:
            mixed: Response from the API. Successful operation

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(organization_id=options.get("organization_id"),
                                 license_id=options.get("license_id"))

        # Prepare query URL
        _url_path = '/organizations/{organizationId}/licenses/{licenseId}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'organizationId': options.get('organization_id', None),
            'licenseId': options.get('license_id', None)
        })
        _query_builder = Configuration.base_uri
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'content-type': 'application/json; charset=utf-8'
        }

        # Prepare and execute request
        _request = self.http_client.put(_query_url, headers=_headers, parameters=APIHelper.json_serialize(options.get('update_organization_license')))
        CustomHeaderAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body)

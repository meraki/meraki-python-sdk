# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""

from meraki.api_helper import APIHelper
from meraki.configuration import Configuration
from meraki.controllers.base_controller import BaseController
from meraki.http.auth.custom_header_auth import CustomHeaderAuth

class OrganizationsController(BaseController):

    """A Controller to access Endpoints in the meraki API."""


    def get_organizations(self):
        """Does a GET request to /organizations.

        List the organizations that the user has privileges on

        Returns:
            mixed: Response from the API. Successful operation

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/organizations'
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

    def create_organization(self,
                            create_organization):
        """Does a POST request to /organizations.

        Create a new organization

        Args:
            create_organization (CreateOrganizationModel): TODO: type
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
        self.validate_parameters(create_organization=create_organization)

        # Prepare query URL
        _url_path = '/organizations'
        _query_builder = Configuration.base_uri
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'content-type': 'application/json; charset=utf-8'
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(create_organization))
        CustomHeaderAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body)

    def get_organization(self,
                         organization_id):
        """Does a GET request to /organizations/{organizationId}.

        Return an organization

        Args:
            organization_id (string): TODO: type description here. Example: 

        Returns:
            mixed: Response from the API. Successful operation

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(organization_id=organization_id)

        # Prepare query URL
        _url_path = '/organizations/{organizationId}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'organizationId': organization_id
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

    def update_organization(self,
                            options=dict()):
        """Does a PUT request to /organizations/{organizationId}.

        Update an organization

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    organization_id -- string -- TODO: type description here.
                        Example: 
                    update_organization -- UpdateOrganizationModel -- TODO:
                        type description here. Example: 

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
        _url_path = '/organizations/{organizationId}'
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
        _request = self.http_client.put(_query_url, headers=_headers, parameters=APIHelper.json_serialize(options.get('update_organization')))
        CustomHeaderAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body)

    def delete_organization(self,
                            organization_id):
        """Does a DELETE request to /organizations/{organizationId}.

        Delete an organization

        Args:
            organization_id (string): TODO: type description here. Example: 

        Returns:
            void: Response from the API. Successful operation

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(organization_id=organization_id)

        # Prepare query URL
        _url_path = '/organizations/{organizationId}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'organizationId': organization_id
        })
        _query_builder = Configuration.base_uri
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare and execute request
        _request = self.http_client.delete(_query_url)
        CustomHeaderAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

    def claim_organization(self,
                           options=dict()):
        """Does a POST request to /organizations/{organizationId}/claim.

        Claim a list of devices, licenses, and/or orders into an organization.
        When claiming by order, all devices and licenses in the order will be
        claimed; licenses will be added to the organization and devices will
        be placed in the organization's inventory.

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    organization_id -- string -- TODO: type description here.
                        Example: 
                    claim_organization -- ClaimOrganizationModel -- TODO: type
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
        self.validate_parameters(organization_id=options.get("organization_id"))

        # Prepare query URL
        _url_path = '/organizations/{organizationId}/claim'
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
        _request = self.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(options.get('claim_organization')))
        CustomHeaderAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body)

    def clone_organization(self,
                           options=dict()):
        """Does a POST request to /organizations/{organizationId}/clone.

        Create a new organization by cloning the addressed organization

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    organization_id -- string -- TODO: type description here.
                        Example: 
                    clone_organization -- CloneOrganizationModel -- TODO: type
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
                                 clone_organization=options.get("clone_organization"))

        # Prepare query URL
        _url_path = '/organizations/{organizationId}/clone'
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
        _request = self.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(options.get('clone_organization')))
        CustomHeaderAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body)

    def get_organization_device_statuses(self,
                                         organization_id):
        """Does a GET request to /organizations/{organizationId}/deviceStatuses.

        List the status of every Meraki device in the organization

        Args:
            organization_id (string): TODO: type description here. Example: 

        Returns:
            mixed: Response from the API. Successful operation

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(organization_id=organization_id)

        # Prepare query URL
        _url_path = '/organizations/{organizationId}/deviceStatuses'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'organizationId': organization_id
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

    def get_organization_inventory(self,
                                   organization_id):
        """Does a GET request to /organizations/{organizationId}/inventory.

        Return the inventory for an organization

        Args:
            organization_id (string): TODO: type description here. Example: 

        Returns:
            mixed: Response from the API. Successful operation

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(organization_id=organization_id)

        # Prepare query URL
        _url_path = '/organizations/{organizationId}/inventory'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'organizationId': organization_id
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

    def get_organization_license_state(self,
                                       organization_id):
        """Does a GET request to /organizations/{organizationId}/licenseState.

        Return the license state for an organization

        Args:
            organization_id (string): TODO: type description here. Example: 

        Returns:
            mixed: Response from the API. Successful operation

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(organization_id=organization_id)

        # Prepare query URL
        _url_path = '/organizations/{organizationId}/licenseState'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'organizationId': organization_id
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

    def get_organization_third_party_vpn_peers(self,
                                               organization_id):
        """Does a GET request to /organizations/{organizationId}/thirdPartyVPNPeers.

        Return the third party VPN peers for an organization

        Args:
            organization_id (string): TODO: type description here. Example: 

        Returns:
            mixed: Response from the API. Successful operation

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(organization_id=organization_id)

        # Prepare query URL
        _url_path = '/organizations/{organizationId}/thirdPartyVPNPeers'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'organizationId': organization_id
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

    def update_organization_third_party_vpn_peers(self,
                                                  options=dict()):
        """Does a PUT request to /organizations/{organizationId}/thirdPartyVPNPeers.

        Update the third party VPN peers for an organization

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    organization_id -- string -- TODO: type description here.
                        Example: 
                    update_organization_third_party_vpn_peers --
                        UpdateOrganizationThirdPartyVPNPeersModel -- TODO:
                        type description here. Example: 

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
                                 update_organization_third_party_vpn_peers=options.get("update_organization_third_party_vpn_peers"))

        # Prepare query URL
        _url_path = '/organizations/{organizationId}/thirdPartyVPNPeers'
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
        _request = self.http_client.put(_query_url, headers=_headers, parameters=APIHelper.json_serialize(options.get('update_organization_third_party_vpn_peers')))
        CustomHeaderAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body)

    def get_organization_uplinks_loss_and_latency(self,
                                                  options=dict()):
        """Does a GET request to /organizations/{organizationId}/uplinksLossAndLatency.

        Return the uplink loss and latency for every MX in the organization
        from at latest 2 minutes ago

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    organization_id -- string -- TODO: type description here.
                        Example: 
                    t_0 -- string -- The beginning of the timespan for the
                        data. The maximum lookback period is 365 days from
                        today.
                    t_1 -- string -- The end of the timespan for the data. t1
                        can be a maximum of 5 minutes after t0. The latest
                        possible time that t1 can be is 2 minutes into the
                        past.
                    timespan -- int -- The timespan for which the information
                        will be fetched. If specifying timespan, do not
                        specify parameters t0 and t1. The value must be in
                        seconds and be less than or equal to 5 minutes. The
                        default is 5 minutes.
                    uplink -- string -- Optional filter for a specific WAN
                        uplink. Valid uplinks are wan1, wan2, cellular.
                        Default will return all uplinks.
                    ip -- string -- Optional filter for a specific destination
                        IP. Default will return all destination IPs.

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
        _url_path = '/organizations/{organizationId}/uplinksLossAndLatency'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'organizationId': options.get('organization_id', None)
        })
        _query_builder = Configuration.base_uri
        _query_builder += _url_path
        _query_parameters = {
            't0': options.get('t0', None),
            't1': options.get('t1', None),
            'timespan': options.get('timespan', None),
            'uplink': options.get('uplink', None),
            'ip': options.get('ip', None)
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

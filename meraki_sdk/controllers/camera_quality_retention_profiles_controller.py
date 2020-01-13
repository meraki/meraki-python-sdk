# -*- coding: utf-8 -*-

"""
    meraki_sdk

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""

from meraki_sdk.api_helper import APIHelper
from meraki_sdk.configuration import Configuration
from meraki_sdk.controllers.base_controller import BaseController
from meraki_sdk.http.auth.custom_header_auth import CustomHeaderAuth

class CameraQualityRetentionProfilesController(BaseController):

    """A Controller to access Endpoints in the meraki_sdk API."""


    def get_network_camera_quality_retention_profiles(self,
                                                      network_id):
        """Does a GET request to /networks/{networkId}/camera/qualityRetentionProfiles.

        List the quality retention profiles for this network

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
        _url_path = '/networks/{networkId}/camera/qualityRetentionProfiles'
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

    def create_network_camera_quality_retention_profile(self,
                                                        options=dict()):
        """Does a POST request to /networks/{networkId}/camera/qualityRetentionProfiles.

        Creates new quality retention profile for this network.

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    network_id -- string -- TODO: type description here.
                        Example: 
                    create_network_camera_quality_retention_profile --
                        CreateNetworkCameraQualityRetentionProfileModel --
                        TODO: type description here. Example: 

        Returns:
            mixed: Response from the API. Successful operation

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(network_id=options.get("network_id"),
                                 create_network_camera_quality_retention_profile=options.get("create_network_camera_quality_retention_profile"))

        # Prepare query URL
        _url_path = '/networks/{networkId}/camera/qualityRetentionProfiles'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'networkId': options.get('network_id', None)
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
        _request = self.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(options.get('create_network_camera_quality_retention_profile')))
        CustomHeaderAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body)

    def get_network_camera_quality_retention_profile(self,
                                                     options=dict()):
        """Does a GET request to /networks/{networkId}/camera/qualityRetentionProfiles/{qualityRetentionProfileId}.

        Retrieve a single quality retention profile

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    network_id -- string -- TODO: type description here.
                        Example: 
                    quality_retention_profile_id -- string -- TODO: type
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
        self.validate_parameters(network_id=options.get("network_id"),
                                 quality_retention_profile_id=options.get("quality_retention_profile_id"))

        # Prepare query URL
        _url_path = '/networks/{networkId}/camera/qualityRetentionProfiles/{qualityRetentionProfileId}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'networkId': options.get('network_id', None),
            'qualityRetentionProfileId': options.get('quality_retention_profile_id', None)
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

    def update_network_camera_quality_retention_profile(self,
                                                        options=dict()):
        """Does a PUT request to /networks/{networkId}/camera/qualityRetentionProfiles/{qualityRetentionProfileId}.

        Update an existing quality retention profile for this network.

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    network_id -- string -- TODO: type description here.
                        Example: 
                    quality_retention_profile_id -- string -- TODO: type
                        description here. Example: 
                    update_network_camera_quality_retention_profile --
                        UpdateNetworkCameraQualityRetentionProfileModel --
                        TODO: type description here. Example: 

        Returns:
            mixed: Response from the API. Successful operation

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(network_id=options.get("network_id"),
                                 quality_retention_profile_id=options.get("quality_retention_profile_id"))

        # Prepare query URL
        _url_path = '/networks/{networkId}/camera/qualityRetentionProfiles/{qualityRetentionProfileId}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'networkId': options.get('network_id', None),
            'qualityRetentionProfileId': options.get('quality_retention_profile_id', None)
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
        _request = self.http_client.put(_query_url, headers=_headers, parameters=APIHelper.json_serialize(options.get('update_network_camera_quality_retention_profile')))
        CustomHeaderAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body)

    def delete_network_camera_quality_retention_profile(self,
                                                        options=dict()):
        """Does a DELETE request to /networks/{networkId}/camera/qualityRetentionProfiles/{qualityRetentionProfileId}.

        Delete an existing quality retention profile for this network.

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    network_id -- string -- TODO: type description here.
                        Example: 
                    quality_retention_profile_id -- string -- TODO: type
                        description here. Example: 

        Returns:
            void: Response from the API. Successful operation

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(network_id=options.get("network_id"),
                                 quality_retention_profile_id=options.get("quality_retention_profile_id"))

        # Prepare query URL
        _url_path = '/networks/{networkId}/camera/qualityRetentionProfiles/{qualityRetentionProfileId}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'networkId': options.get('network_id', None),
            'qualityRetentionProfileId': options.get('quality_retention_profile_id', None)
        })
        _query_builder = Configuration.base_uri
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare and execute request
        _request = self.http_client.delete(_query_url)
        CustomHeaderAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

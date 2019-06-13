# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""

from meraki.api_helper import APIHelper
from meraki.configuration import Configuration
from meraki.controllers.base_controller import BaseController
from meraki.http.auth.custom_header_auth import CustomHeaderAuth

class SwitchProfilesController(BaseController):

    """A Controller to access Endpoints in the meraki API."""


    def get_organization_config_template_switch_profiles(self,
                                                         options=dict()):
        """Does a GET request to /organizations/{organizationId}/configTemplates/{configTemplateId}/switchProfiles.

        List the switch profiles for your switch template configuration

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    organization_id -- string -- TODO: type description here.
                        Example: 
                    config_template_id -- string -- TODO: type description
                        here. Example: 

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
                                 config_template_id=options.get("config_template_id"))

        # Prepare query URL
        _url_path = '/organizations/{organizationId}/configTemplates/{configTemplateId}/switchProfiles'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'organizationId': options.get('organization_id', None),
            'configTemplateId': options.get('config_template_id', None)
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

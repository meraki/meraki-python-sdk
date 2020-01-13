# -*- coding: utf-8 -*-

"""
    meraki_sdk

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""

from meraki_sdk.api_helper import APIHelper
from meraki_sdk.configuration import Configuration
from meraki_sdk.controllers.base_controller import BaseController
from meraki_sdk.http.auth.custom_header_auth import CustomHeaderAuth

class SwitchSettingsController(BaseController):

    """A Controller to access Endpoints in the meraki_sdk API."""


    def get_network_switch_settings(self,
                                    network_id):
        """Does a GET request to /networks/{networkId}/switch/settings.

        Returns the switch network settings

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
        _url_path = '/networks/{networkId}/switch/settings'
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

    def update_network_switch_settings(self,
                                       options=dict()):
        """Does a PUT request to /networks/{networkId}/switch/settings.

        Update switch network settings

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    network_id -- string -- TODO: type description here.
                        Example: 
                    update_network_switch_settings --
                        UpdateNetworkSwitchSettingsModel -- TODO: type
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
        self.validate_parameters(network_id=options.get("network_id"))

        # Prepare query URL
        _url_path = '/networks/{networkId}/switch/settings'
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
        _request = self.http_client.put(_query_url, headers=_headers, parameters=APIHelper.json_serialize(options.get('update_network_switch_settings')))
        CustomHeaderAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body)

    def get_network_switch_settings_dhcp_server_policy(self,
                                                       network_id):
        """Does a GET request to /networks/{networkId}/switch/settings/dhcpServerPolicy.

        Return the DHCP server policy

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
        _url_path = '/networks/{networkId}/switch/settings/dhcpServerPolicy'
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

    def update_network_switch_settings_dhcp_server_policy(self,
                                                          options=dict()):
        """Does a PUT request to /networks/{networkId}/switch/settings/dhcpServerPolicy.

        Update the DHCP server policy

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    network_id -- string -- TODO: type description here.
                        Example: 
                    update_network_switch_settings_dhcp_server_policy --
                        UpdateNetworkSwitchSettingsDhcpServerPolicyModel --
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
        self.validate_parameters(network_id=options.get("network_id"))

        # Prepare query URL
        _url_path = '/networks/{networkId}/switch/settings/dhcpServerPolicy'
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
        _request = self.http_client.put(_query_url, headers=_headers, parameters=APIHelper.json_serialize(options.get('update_network_switch_settings_dhcp_server_policy')))
        CustomHeaderAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body)

    def get_network_switch_settings_dscp_to_cos_mappings(self,
                                                         network_id):
        """Does a GET request to /networks/{networkId}/switch/settings/dscpToCosMappings.

        Return the DSCP to CoS mappings

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
        _url_path = '/networks/{networkId}/switch/settings/dscpToCosMappings'
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

    def update_network_switch_settings_dscp_to_cos_mappings(self,
                                                            options=dict()):
        """Does a PUT request to /networks/{networkId}/switch/settings/dscpToCosMappings.

        Update the DSCP to CoS mappings

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    network_id -- string -- TODO: type description here.
                        Example: 
                    update_network_switch_settings_dscp_to_cos_mappings --
                        UpdateNetworkSwitchSettingsDscpToCosMappingsModel --
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
                                 update_network_switch_settings_dscp_to_cos_mappings=options.get("update_network_switch_settings_dscp_to_cos_mappings"))

        # Prepare query URL
        _url_path = '/networks/{networkId}/switch/settings/dscpToCosMappings'
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
        _request = self.http_client.put(_query_url, headers=_headers, parameters=APIHelper.json_serialize(options.get('update_network_switch_settings_dscp_to_cos_mappings')))
        CustomHeaderAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body)

    def get_network_switch_settings_mtu(self,
                                        network_id):
        """Does a GET request to /networks/{networkId}/switch/settings/mtu.

        Return the MTU configuration

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
        _url_path = '/networks/{networkId}/switch/settings/mtu'
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

    def update_network_switch_settings_mtu(self,
                                           options=dict()):
        """Does a PUT request to /networks/{networkId}/switch/settings/mtu.

        Update the MTU configuration

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    network_id -- string -- TODO: type description here.
                        Example: 
                    update_network_switch_settings_mtu --
                        UpdateNetworkSwitchSettingsMtuModel -- TODO: type
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
        self.validate_parameters(network_id=options.get("network_id"))

        # Prepare query URL
        _url_path = '/networks/{networkId}/switch/settings/mtu'
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
        _request = self.http_client.put(_query_url, headers=_headers, parameters=APIHelper.json_serialize(options.get('update_network_switch_settings_mtu')))
        CustomHeaderAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body)

    def get_network_switch_settings_qos_rules(self,
                                              network_id):
        """Does a GET request to /networks/{networkId}/switch/settings/qosRules.

        List quality of service rules

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
        _url_path = '/networks/{networkId}/switch/settings/qosRules'
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

    def create_network_switch_settings_qos_rule(self,
                                                options=dict()):
        """Does a POST request to /networks/{networkId}/switch/settings/qosRules.

        Add a quality of service rule

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    network_id -- string -- TODO: type description here.
                        Example: 
                    create_network_switch_settings_qos_rule --
                        CreateNetworkSwitchSettingsQosRuleModel -- TODO: type
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
                                 create_network_switch_settings_qos_rule=options.get("create_network_switch_settings_qos_rule"))

        # Prepare query URL
        _url_path = '/networks/{networkId}/switch/settings/qosRules'
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
        _request = self.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(options.get('create_network_switch_settings_qos_rule')))
        CustomHeaderAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body)

    def get_network_switch_settings_qos_rules_order(self,
                                                    network_id):
        """Does a GET request to /networks/{networkId}/switch/settings/qosRules/order.

        Return the quality of service rule IDs by order in which they will be
        processed by the switch

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
        _url_path = '/networks/{networkId}/switch/settings/qosRules/order'
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

    def update_network_switch_settings_qos_rules_order(self,
                                                       options=dict()):
        """Does a PUT request to /networks/{networkId}/switch/settings/qosRules/order.

        Update the order in which the rules should be processed by the switch

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    network_id -- string -- TODO: type description here.
                        Example: 
                    update_network_switch_settings_qos_rules_order --
                        UpdateNetworkSwitchSettingsQosRulesOrderModel -- TODO:
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
        self.validate_parameters(network_id=options.get("network_id"),
                                 update_network_switch_settings_qos_rules_order=options.get("update_network_switch_settings_qos_rules_order"))

        # Prepare query URL
        _url_path = '/networks/{networkId}/switch/settings/qosRules/order'
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
        _request = self.http_client.put(_query_url, headers=_headers, parameters=APIHelper.json_serialize(options.get('update_network_switch_settings_qos_rules_order')))
        CustomHeaderAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body)

    def get_network_switch_settings_qos_rule(self,
                                             options=dict()):
        """Does a GET request to /networks/{networkId}/switch/settings/qosRules/{qosRuleId}.

        Return a quality of service rule

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    network_id -- string -- TODO: type description here.
                        Example: 
                    qos_rule_id -- string -- TODO: type description here.
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
        self.validate_parameters(network_id=options.get("network_id"),
                                 qos_rule_id=options.get("qos_rule_id"))

        # Prepare query URL
        _url_path = '/networks/{networkId}/switch/settings/qosRules/{qosRuleId}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'networkId': options.get('network_id', None),
            'qosRuleId': options.get('qos_rule_id', None)
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

    def delete_network_switch_settings_qos_rule(self,
                                                options=dict()):
        """Does a DELETE request to /networks/{networkId}/switch/settings/qosRules/{qosRuleId}.

        Delete a quality of service rule

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    network_id -- string -- TODO: type description here.
                        Example: 
                    qos_rule_id -- string -- TODO: type description here.
                        Example: 

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
                                 qos_rule_id=options.get("qos_rule_id"))

        # Prepare query URL
        _url_path = '/networks/{networkId}/switch/settings/qosRules/{qosRuleId}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'networkId': options.get('network_id', None),
            'qosRuleId': options.get('qos_rule_id', None)
        })
        _query_builder = Configuration.base_uri
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare and execute request
        _request = self.http_client.delete(_query_url)
        CustomHeaderAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

    def update_network_switch_settings_qos_rule(self,
                                                options=dict()):
        """Does a PUT request to /networks/{networkId}/switch/settings/qosRules/{qosRuleId}.

        Update a quality of service rule

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    network_id -- string -- TODO: type description here.
                        Example: 
                    qos_rule_id -- string -- TODO: type description here.
                        Example: 
                    update_network_switch_settings_qos_rule --
                        UpdateNetworkSwitchSettingsQosRuleModel -- TODO: type
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
                                 qos_rule_id=options.get("qos_rule_id"))

        # Prepare query URL
        _url_path = '/networks/{networkId}/switch/settings/qosRules/{qosRuleId}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'networkId': options.get('network_id', None),
            'qosRuleId': options.get('qos_rule_id', None)
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
        _request = self.http_client.put(_query_url, headers=_headers, parameters=APIHelper.json_serialize(options.get('update_network_switch_settings_qos_rule')))
        CustomHeaderAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body)

    def get_network_switch_settings_storm_control(self,
                                                  network_id):
        """Does a GET request to /networks/{networkId}/switch/settings/stormControl.

        Return the storm control configuration for a switch network

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
        _url_path = '/networks/{networkId}/switch/settings/stormControl'
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

    def update_network_switch_settings_storm_control(self,
                                                     options=dict()):
        """Does a PUT request to /networks/{networkId}/switch/settings/stormControl.

        Update the storm control configuration for a switch network

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    network_id -- string -- TODO: type description here.
                        Example: 
                    update_network_switch_settings_storm_control --
                        UpdateNetworkSwitchSettingsStormControlModel -- TODO:
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
        self.validate_parameters(network_id=options.get("network_id"))

        # Prepare query URL
        _url_path = '/networks/{networkId}/switch/settings/stormControl'
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
        _request = self.http_client.put(_query_url, headers=_headers, parameters=APIHelper.json_serialize(options.get('update_network_switch_settings_storm_control')))
        CustomHeaderAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body)

    def get_network_switch_settings_stp(self,
                                        network_id):
        """Does a GET request to /networks/{networkId}/switch/settings/stp.

        Returns STP settings

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
        _url_path = '/networks/{networkId}/switch/settings/stp'
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

    def update_network_switch_settings_stp(self,
                                           options=dict()):
        """Does a PUT request to /networks/{networkId}/switch/settings/stp.

        Updates STP settings

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    network_id -- string -- TODO: type description here.
                        Example: 
                    update_network_switch_settings_stp --
                        UpdateNetworkSwitchSettingsStpModel -- TODO: type
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
        self.validate_parameters(network_id=options.get("network_id"))

        # Prepare query URL
        _url_path = '/networks/{networkId}/switch/settings/stp'
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
        _request = self.http_client.put(_query_url, headers=_headers, parameters=APIHelper.json_serialize(options.get('update_network_switch_settings_stp')))
        CustomHeaderAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body)

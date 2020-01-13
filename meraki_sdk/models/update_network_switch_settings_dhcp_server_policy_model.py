# -*- coding: utf-8 -*-

"""
    meraki_sdk

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class UpdateNetworkSwitchSettingsDhcpServerPolicyModel(object):

    """Implementation of the 'updateNetworkSwitchSettingsDhcpServerPolicy' model.

    TODO: type model description here.

    Attributes:
        default_policy (DefaultPolicyEnum): 'allow' or 'block' new DHCP
            servers. Default value is 'allow'.
        allowed_servers (list of string): List the MAC addresses of DHCP
            servers to permit on the network. Applicable only if defaultPolicy
            is set to block. An empty array will clear the entries.
        blocked_servers (list of string): List the MAC addresses of DHCP
            servers to block on the network. Applicable only if defaultPolicy
            is set to allow. An empty array will clear the entries.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "default_policy":'defaultPolicy',
        "allowed_servers":'allowedServers',
        "blocked_servers":'blockedServers'
    }

    def __init__(self,
                 default_policy=None,
                 allowed_servers=None,
                 blocked_servers=None):
        """Constructor for the UpdateNetworkSwitchSettingsDhcpServerPolicyModel class"""

        # Initialize members of the class
        self.default_policy = default_policy
        self.allowed_servers = allowed_servers
        self.blocked_servers = blocked_servers


    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object as
            obtained from the deserialization of the server's response. The keys
            MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary
        default_policy = dictionary.get('defaultPolicy')
        allowed_servers = dictionary.get('allowedServers')
        blocked_servers = dictionary.get('blockedServers')

        # Return an object of this model
        return cls(default_policy,
                   allowed_servers,
                   blocked_servers)



# -*- coding: utf-8 -*-

"""
    meraki_sdk

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class ProvisionNetworkClientsModel(object):

    """Implementation of the 'provisionNetworkClients' model.

    TODO: type model description here.

    Attributes:
        mac (string): The MAC address of the client. Required.
        name (string): The display name for the client. Optional. Limited to
            255 bytes.
        device_policy (DevicePolicyEnum): The policy to apply to the specified
            client. Can be 'Whitelisted', 'Blocked', 'Normal' or 'Group
            policy'. Required.
        group_policy_id (int): The ID of the desired group policy to apply to
            the client. Required if 'devicePolicy' is set to "Group policy".
            Otherwise this is ignored.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "mac":'mac',
        "device_policy":'devicePolicy',
        "name":'name',
        "group_policy_id":'groupPolicyId'
    }

    def __init__(self,
                 mac=None,
                 device_policy=None,
                 name=None,
                 group_policy_id=None):
        """Constructor for the ProvisionNetworkClientsModel class"""

        # Initialize members of the class
        self.mac = mac
        self.name = name
        self.device_policy = device_policy
        self.group_policy_id = group_policy_id


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
        mac = dictionary.get('mac')
        device_policy = dictionary.get('devicePolicy')
        name = dictionary.get('name')
        group_policy_id = dictionary.get('groupPolicyId')

        # Return an object of this model
        return cls(mac,
                   device_policy,
                   name,
                   group_policy_id)



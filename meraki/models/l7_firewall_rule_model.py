# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class L7FirewallRuleModel(object):

    """Implementation of the 'L7FirewallRule' model.

    TODO: type model description here.

    Attributes:
        policy (Policy1Enum): The policy applied to matching traffic. Must be
            'deny'.
        mtype (Type2Enum): Type of the L7 Rule. Must be 'application',
            'applicationCategory', 'host', 'port' or 'ipRange'
        value (string): The 'value' of what you want to block. If 'type' is
            'host', 'port' or 'ipRange', 'value' must be a string matching
            either a hostname (e.g. somewhere.com), a port (e.g. 8080), or an
            IP range (e.g. 192.1.0.0/16). If 'type' is 'application' or
            'applicationCategory', then 'value' must be an object with an ID
            for the application.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "policy":'policy',
        "mtype":'type',
        "value":'value'
    }

    def __init__(self,
                 policy=None,
                 mtype=None,
                 value=None):
        """Constructor for the L7FirewallRuleModel class"""

        # Initialize members of the class
        self.policy = policy
        self.mtype = mtype
        self.value = value


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
        policy = dictionary.get('policy')
        mtype = dictionary.get('type')
        value = dictionary.get('value')

        # Return an object of this model
        return cls(policy,
                   mtype,
                   value)



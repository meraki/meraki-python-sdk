# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class ProtectedNetworksModel(object):

    """Implementation of the 'ProtectedNetworks' model.

    Set the included/excluded networks from the intrusion engine (optional -
    omitting will leave current config unchanged)

    Attributes:
        use_default (bool): true/false whether to use special IPv4 addresses:
            https://tools.ietf.org/html/rfc5735 (required). Default value is
            true if none currently saved
        included_cidr (list of string): list of IP addresses or subnets being
            protected (required if 'useDefault' is false)
        excluded_cidr (list of string): list of IP addresses or subnets being
            excluded from protection (required if 'useDefault' is false)

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "use_default":'useDefault',
        "included_cidr":'includedCidr',
        "excluded_cidr":'excludedCidr'
    }

    def __init__(self,
                 use_default=None,
                 included_cidr=None,
                 excluded_cidr=None):
        """Constructor for the ProtectedNetworksModel class"""

        # Initialize members of the class
        self.use_default = use_default
        self.included_cidr = included_cidr
        self.excluded_cidr = excluded_cidr


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
        use_default = dictionary.get('useDefault')
        included_cidr = dictionary.get('includedCidr')
        excluded_cidr = dictionary.get('excludedCidr')

        # Return an object of this model
        return cls(use_default,
                   included_cidr,
                   excluded_cidr)



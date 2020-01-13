# -*- coding: utf-8 -*-

"""
    meraki_sdk

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class UpdateNetworkCellularGatewaySettingsSubnetPoolModel(object):

    """Implementation of the 'updateNetworkCellularGatewaySettingsSubnetPool' model.

    TODO: type model description here.

    Attributes:
        mask (int): Mask used for the subnet of all MGs in  this network.
        cidr (string): CIDR of the pool of subnets. Each MG in this network
            will automatically pick a subnet from this pool.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "mask":'mask',
        "cidr":'cidr'
    }

    def __init__(self,
                 mask=None,
                 cidr=None):
        """Constructor for the UpdateNetworkCellularGatewaySettingsSubnetPoolModel class"""

        # Initialize members of the class
        self.mask = mask
        self.cidr = cidr


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
        mask = dictionary.get('mask')
        cidr = dictionary.get('cidr')

        # Return an object of this model
        return cls(mask,
                   cidr)



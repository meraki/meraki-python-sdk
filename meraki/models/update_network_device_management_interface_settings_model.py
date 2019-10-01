# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""

import meraki.models.wan_1_model
import meraki.models.wan_2_model

class UpdateNetworkDeviceManagementInterfaceSettingsModel(object):

    """Implementation of the 'updateNetworkDeviceManagementInterfaceSettings' model.

    TODO: type model description here.

    Attributes:
        wan_1 (Wan1Model): WAN 1 settings
        wan_2 (Wan2Model): WAN 2 settings (only for MX devices)

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "wan_1":'wan1',
        "wan_2":'wan2'
    }

    def __init__(self,
                 wan_1=None,
                 wan_2=None):
        """Constructor for the UpdateNetworkDeviceManagementInterfaceSettingsModel class"""

        # Initialize members of the class
        self.wan_1 = wan_1
        self.wan_2 = wan_2


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
        wan_1 = meraki.models.wan_1_model.Wan1Model.from_dictionary(dictionary.get('wan1')) if dictionary.get('wan1') else None
        wan_2 = meraki.models.wan_2_model.Wan2Model.from_dictionary(dictionary.get('wan2')) if dictionary.get('wan2') else None

        # Return an object of this model
        return cls(wan_1,
                   wan_2)



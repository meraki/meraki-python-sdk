# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""

import meraki.models.ssids_model

class UpdateNetworkClientSplashAuthorizationStatusModel(object):

    """Implementation of the 'updateNetworkClientSplashAuthorizationStatus' model.

    TODO: type model description here.

    Attributes:
        ssids (SsidsModel): The target SSIDs. For each SSID where isAuthorized
            is true, the expiration time will automatically be set according
            to the SSID's splash frequency.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "ssids":'ssids'
    }

    def __init__(self,
                 ssids=None):
        """Constructor for the UpdateNetworkClientSplashAuthorizationStatusModel class"""

        # Initialize members of the class
        self.ssids = ssids


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
        ssids = meraki.models.ssids_model.SsidsModel.from_dictionary(dictionary.get('ssids')) if dictionary.get('ssids') else None

        # Return an object of this model
        return cls(ssids)



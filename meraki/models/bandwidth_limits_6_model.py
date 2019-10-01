# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""

import meraki.models.wan_11_model
import meraki.models.wan_21_model
import meraki.models.cellular_model

class BandwidthLimits6Model(object):

    """Implementation of the 'BandwidthLimits6' model.

    A mapping of uplinks to their bandwidth settings (be sure to check which
    uplinks are supported for your network)

    Attributes:
        wan_1 (Wan11Model): The bandwidth settings for the 'wan1' uplink
        wan_2 (Wan21Model): The bandwidth settings for the 'wan2' uplink
        cellular (CellularModel): The bandwidth settings for the 'cellular'
            uplink

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "wan_1":'wan1',
        "wan_2":'wan2',
        "cellular":'cellular'
    }

    def __init__(self,
                 wan_1=None,
                 wan_2=None,
                 cellular=None):
        """Constructor for the BandwidthLimits6Model class"""

        # Initialize members of the class
        self.wan_1 = wan_1
        self.wan_2 = wan_2
        self.cellular = cellular


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
        wan_1 = meraki.models.wan_11_model.Wan11Model.from_dictionary(dictionary.get('wan1')) if dictionary.get('wan1') else None
        wan_2 = meraki.models.wan_21_model.Wan21Model.from_dictionary(dictionary.get('wan2')) if dictionary.get('wan2') else None
        cellular = meraki.models.cellular_model.CellularModel.from_dictionary(dictionary.get('cellular')) if dictionary.get('cellular') else None

        # Return an object of this model
        return cls(wan_1,
                   wan_2,
                   cellular)



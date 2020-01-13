# -*- coding: utf-8 -*-

"""
    meraki_sdk

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""

import meraki_sdk.models.mapping_model

class UpdateNetworkSwitchSettingsDscpToCosMappingsModel(object):

    """Implementation of the 'updateNetworkSwitchSettingsDscpToCosMappings' model.

    TODO: type model description here.

    Attributes:
        mappings (list of MappingModel): An array of DSCP to CoS mappings. An
            empty array will reset the mappings to default.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "mappings":'mappings'
    }

    def __init__(self,
                 mappings=None):
        """Constructor for the UpdateNetworkSwitchSettingsDscpToCosMappingsModel class"""

        # Initialize members of the class
        self.mappings = mappings


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
        mappings = None
        if dictionary.get('mappings') != None:
            mappings = list()
            for structure in dictionary.get('mappings'):
                mappings.append(meraki_sdk.models.mapping_model.MappingModel.from_dictionary(structure))

        # Return an object of this model
        return cls(mappings)



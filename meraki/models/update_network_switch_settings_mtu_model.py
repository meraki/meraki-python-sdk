# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""

import meraki.models.override_model

class UpdateNetworkSwitchSettingsMtuModel(object):

    """Implementation of the 'updateNetworkSwitchSettingsMtu' model.

    TODO: type model description here.

    Attributes:
        default_mtu_size (int): MTU size for the entire network. Default value
            is 9578.
        overrides (list of OverrideModel): Override MTU size for individual
            switches or switch profiles. An empty array will clear overrides.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "default_mtu_size":'defaultMtuSize',
        "overrides":'overrides'
    }

    def __init__(self,
                 default_mtu_size=None,
                 overrides=None):
        """Constructor for the UpdateNetworkSwitchSettingsMtuModel class"""

        # Initialize members of the class
        self.default_mtu_size = default_mtu_size
        self.overrides = overrides


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
        default_mtu_size = dictionary.get('defaultMtuSize')
        overrides = None
        if dictionary.get('overrides') != None:
            overrides = list()
            for structure in dictionary.get('overrides'):
                overrides.append(meraki.models.override_model.OverrideModel.from_dictionary(structure))

        # Return an object of this model
        return cls(default_mtu_size,
                   overrides)



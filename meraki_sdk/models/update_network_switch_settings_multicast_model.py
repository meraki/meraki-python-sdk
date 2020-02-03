# -*- coding: utf-8 -*-

"""
    meraki_sdk

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""

import meraki_sdk.models.default_settings_model
import meraki_sdk.models.override_1_model

class UpdateNetworkSwitchSettingsMulticastModel(object):

    """Implementation of the 'updateNetworkSwitchSettingsMulticast' model.

    TODO: type model description here.

    Attributes:
        default_settings (DefaultSettingsModel): Default multicast setting for
            entire network. IGMP snooping and Flood unknown multicast traffic
            settings are enabled by default.
        overrides (list of Override1Model): Array of paired
            switches/stacks/profiles and corresponding multicast settings. An
            empty array will clear the multicast settings.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "default_settings":'defaultSettings',
        "overrides":'overrides'
    }

    def __init__(self,
                 default_settings=None,
                 overrides=None):
        """Constructor for the UpdateNetworkSwitchSettingsMulticastModel class"""

        # Initialize members of the class
        self.default_settings = default_settings
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
        default_settings = meraki_sdk.models.default_settings_model.DefaultSettingsModel.from_dictionary(dictionary.get('defaultSettings')) if dictionary.get('defaultSettings') else None
        overrides = None
        if dictionary.get('overrides') != None:
            overrides = list()
            for structure in dictionary.get('overrides'):
                overrides.append(meraki_sdk.models.override_1_model.Override1Model.from_dictionary(structure))

        # Return an object of this model
        return cls(default_settings,
                   overrides)



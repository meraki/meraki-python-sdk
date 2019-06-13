# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""

import meraki.models.bandwidth_limits1_model

class PerClientBandwidthLimitsModel(object):

    """Implementation of the 'PerClientBandwidthLimits' model.

    An object describing the bandwidth settings for your rule.

    Attributes:
        settings (string): How bandwidth limits are applied by your rule. Can
            be one of 'network default', 'ignore' or 'custom'.
        bandwidth_limits (BandwidthLimits1Model): The bandwidth limits object,
            specifying the upload ('limitUp') and download ('limitDown') speed
            in Kbps. These are only enforced if 'settings' is set to
            'custom'.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "settings":'settings',
        "bandwidth_limits":'bandwidthLimits'
    }

    def __init__(self,
                 settings=None,
                 bandwidth_limits=None):
        """Constructor for the PerClientBandwidthLimitsModel class"""

        # Initialize members of the class
        self.settings = settings
        self.bandwidth_limits = bandwidth_limits


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
        settings = dictionary.get('settings')
        bandwidth_limits = meraki.models.bandwidth_limits1_model.BandwidthLimits1Model.from_dictionary(dictionary.get('bandwidthLimits')) if dictionary.get('bandwidthLimits') else None

        # Return an object of this model
        return cls(settings,
                   bandwidth_limits)



# -*- coding: utf-8 -*-

"""
    meraki_sdk

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""

import meraki_sdk.models.bandwidth_limits_model

class UpdateNetworkCellularGatewaySettingsUplinkModel(object):

    """Implementation of the 'updateNetworkCellularGatewaySettingsUplink' model.

    TODO: type model description here.

    Attributes:
        bandwidth_limits (BandwidthLimitsModel): The bandwidth settings for
            the 'cellular' uplink

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "bandwidth_limits":'bandwidthLimits'
    }

    def __init__(self,
                 bandwidth_limits=None):
        """Constructor for the UpdateNetworkCellularGatewaySettingsUplinkModel class"""

        # Initialize members of the class
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
        bandwidth_limits = meraki_sdk.models.bandwidth_limits_model.BandwidthLimitsModel.from_dictionary(dictionary.get('bandwidthLimits')) if dictionary.get('bandwidthLimits') else None

        # Return an object of this model
        return cls(bandwidth_limits)



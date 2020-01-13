# -*- coding: utf-8 -*-

"""
    meraki_sdk

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class UpdateNetworkSwitchSettingsStormControlModel(object):

    """Implementation of the 'updateNetworkSwitchSettingsStormControl' model.

    TODO: type model description here.

    Attributes:
        broadcast_threshold (int): Percentage (1 to 99) of total available
            port bandwidth for broadcast traffic type. Default value 100
            percent rate is to clear the configuration.
        multicast_threshold (int): Percentage (1 to 99) of total available
            port bandwidth for multicast traffic type. Default value 100
            percent rate is to clear the configuration.
        unknown_unicast_threshold (int): Percentage (1 to 99) of total
            available port bandwidth for unknown unicast (dlf-destination
            lookup failure) traffic type. Default value 100 percent rate is to
            clear the configuration.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "broadcast_threshold":'broadcastThreshold',
        "multicast_threshold":'multicastThreshold',
        "unknown_unicast_threshold":'unknownUnicastThreshold'
    }

    def __init__(self,
                 broadcast_threshold=None,
                 multicast_threshold=None,
                 unknown_unicast_threshold=None):
        """Constructor for the UpdateNetworkSwitchSettingsStormControlModel class"""

        # Initialize members of the class
        self.broadcast_threshold = broadcast_threshold
        self.multicast_threshold = multicast_threshold
        self.unknown_unicast_threshold = unknown_unicast_threshold


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
        broadcast_threshold = dictionary.get('broadcastThreshold')
        multicast_threshold = dictionary.get('multicastThreshold')
        unknown_unicast_threshold = dictionary.get('unknownUnicastThreshold')

        # Return an object of this model
        return cls(broadcast_threshold,
                   multicast_threshold,
                   unknown_unicast_threshold)



# -*- coding: utf-8 -*-

"""
    meraki_sdk

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class DefaultSettingsModel(object):

    """Implementation of the 'DefaultSettings' model.

    Default multicast setting for entire network. IGMP snooping and Flood
    unknown multicast traffic settings are enabled by default.

    Attributes:
        igmp_snooping_enabled (bool): IGMP snooping setting for entire
            network
        flood_unknown_multicast_traffic_enabled (bool): Flood unknown
            multicast traffic setting for entire network

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "igmp_snooping_enabled":'igmpSnoopingEnabled',
        "flood_unknown_multicast_traffic_enabled":'floodUnknownMulticastTrafficEnabled'
    }

    def __init__(self,
                 igmp_snooping_enabled=None,
                 flood_unknown_multicast_traffic_enabled=None):
        """Constructor for the DefaultSettingsModel class"""

        # Initialize members of the class
        self.igmp_snooping_enabled = igmp_snooping_enabled
        self.flood_unknown_multicast_traffic_enabled = flood_unknown_multicast_traffic_enabled


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
        igmp_snooping_enabled = dictionary.get('igmpSnoopingEnabled')
        flood_unknown_multicast_traffic_enabled = dictionary.get('floodUnknownMulticastTrafficEnabled')

        # Return an object of this model
        return cls(igmp_snooping_enabled,
                   flood_unknown_multicast_traffic_enabled)



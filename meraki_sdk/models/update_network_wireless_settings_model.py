# -*- coding: utf-8 -*-

"""
    meraki_sdk

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class UpdateNetworkWirelessSettingsModel(object):

    """Implementation of the 'updateNetworkWirelessSettings' model.

    TODO: type model description here.

    Attributes:
        meshing_enabled (bool): Toggle for enabling or disabling meshing in a
            network
        ipv_6_bridge_enabled (bool): Toggle for enabling or disabling IPv6
            bridging in a network (Note: if enabled, SSIDs must also be
            configured to use bridge mode)
        location_analytics_enabled (bool): Toggle for enabling or disabling
            location analytics for your network
        led_lights_on (bool): Toggle for enabling or disabling LED lights on
            all APs in the network (making them run dark)

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "meshing_enabled":'meshingEnabled',
        "ipv_6_bridge_enabled":'ipv6BridgeEnabled',
        "location_analytics_enabled":'locationAnalyticsEnabled',
        "led_lights_on":'ledLightsOn'
    }

    def __init__(self,
                 meshing_enabled=None,
                 ipv_6_bridge_enabled=None,
                 location_analytics_enabled=None,
                 led_lights_on=None):
        """Constructor for the UpdateNetworkWirelessSettingsModel class"""

        # Initialize members of the class
        self.meshing_enabled = meshing_enabled
        self.ipv_6_bridge_enabled = ipv_6_bridge_enabled
        self.location_analytics_enabled = location_analytics_enabled
        self.led_lights_on = led_lights_on


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
        meshing_enabled = dictionary.get('meshingEnabled')
        ipv_6_bridge_enabled = dictionary.get('ipv6BridgeEnabled')
        location_analytics_enabled = dictionary.get('locationAnalyticsEnabled')
        led_lights_on = dictionary.get('ledLightsOn')

        # Return an object of this model
        return cls(meshing_enabled,
                   ipv_6_bridge_enabled,
                   location_analytics_enabled,
                   led_lights_on)



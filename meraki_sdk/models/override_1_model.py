# -*- coding: utf-8 -*-

"""
    meraki_sdk

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class Override1Model(object):

    """Implementation of the 'Override1' model.

    TODO: type model description here.

    Attributes:
        switch_profiles (list of string): List of switch profiles ids for
            template network
        switches (list of string): List of switch serials for non-template
            network
        stacks (list of string): List of switch stack ids for non-template
            network
        igmp_snooping_enabled (bool): IGMP snooping setting for switches,
            switch stacks or switch profiles
        flood_unknown_multicast_traffic_enabled (bool): Flood unknown
            multicast traffic setting for switches, switch stacks or switch
            profiles

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "igmp_snooping_enabled":'igmpSnoopingEnabled',
        "flood_unknown_multicast_traffic_enabled":'floodUnknownMulticastTrafficEnabled',
        "switch_profiles":'switchProfiles',
        "switches":'switches',
        "stacks":'stacks'
    }

    def __init__(self,
                 igmp_snooping_enabled=None,
                 flood_unknown_multicast_traffic_enabled=None,
                 switch_profiles=None,
                 switches=None,
                 stacks=None):
        """Constructor for the Override1Model class"""

        # Initialize members of the class
        self.switch_profiles = switch_profiles
        self.switches = switches
        self.stacks = stacks
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
        switch_profiles = dictionary.get('switchProfiles')
        switches = dictionary.get('switches')
        stacks = dictionary.get('stacks')

        # Return an object of this model
        return cls(igmp_snooping_enabled,
                   flood_unknown_multicast_traffic_enabled,
                   switch_profiles,
                   switches,
                   stacks)



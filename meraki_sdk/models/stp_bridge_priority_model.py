# -*- coding: utf-8 -*-

"""
    meraki_sdk

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class StpBridgePriorityModel(object):

    """Implementation of the 'StpBridgePriority' model.

    TODO: type model description here.

    Attributes:
        switch_profiles (list of string): List of switch profile IDs
        switches (list of string): List of switch serial numbers
        stacks (list of string): List of stack IDs
        stp_priority (int): STP priority for switch, stacks, or switch
            profiles

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "stp_priority":'stpPriority',
        "switch_profiles":'switchProfiles',
        "switches":'switches',
        "stacks":'stacks'
    }

    def __init__(self,
                 stp_priority=None,
                 switch_profiles=None,
                 switches=None,
                 stacks=None):
        """Constructor for the StpBridgePriorityModel class"""

        # Initialize members of the class
        self.switch_profiles = switch_profiles
        self.switches = switches
        self.stacks = stacks
        self.stp_priority = stp_priority


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
        stp_priority = dictionary.get('stpPriority')
        switch_profiles = dictionary.get('switchProfiles')
        switches = dictionary.get('switches')
        stacks = dictionary.get('stacks')

        # Return an object of this model
        return cls(stp_priority,
                   switch_profiles,
                   switches,
                   stacks)



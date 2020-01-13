# -*- coding: utf-8 -*-

"""
    meraki_sdk

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class OverrideModel(object):

    """Implementation of the 'Override' model.

    TODO: type model description here.

    Attributes:
        switches (list of string): List of switch serials. Applicable only for
            switch network.
        switch_profiles (list of string): List of switch profile IDs.
            Applicable only for template network.
        mtu_size (int): MTU size for the switches or switch profiles.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "mtu_size":'mtuSize',
        "switches":'switches',
        "switch_profiles":'switchProfiles'
    }

    def __init__(self,
                 mtu_size=None,
                 switches=None,
                 switch_profiles=None):
        """Constructor for the OverrideModel class"""

        # Initialize members of the class
        self.switches = switches
        self.switch_profiles = switch_profiles
        self.mtu_size = mtu_size


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
        mtu_size = dictionary.get('mtuSize')
        switches = dictionary.get('switches')
        switch_profiles = dictionary.get('switchProfiles')

        # Return an object of this model
        return cls(mtu_size,
                   switches,
                   switch_profiles)



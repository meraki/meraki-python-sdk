# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class VlanTaggingModel(object):

    """Implementation of the 'VlanTagging' model.

    The VLAN tagging settings for your group policy. Only available if your
    network has a wireless configuration.

    Attributes:
        settings (Settings2Enum): How VLAN tagging is applied. Can be 'network
            default', 'ignore' or 'custom'.
        vlan_id (string): The ID of the vlan you want to tag. This only
            applies if 'settings' is set to 'custom'.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "settings":'settings',
        "vlan_id":'vlanId'
    }

    def __init__(self,
                 settings=None,
                 vlan_id=None):
        """Constructor for the VlanTaggingModel class"""

        # Initialize members of the class
        self.settings = settings
        self.vlan_id = vlan_id


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
        vlan_id = dictionary.get('vlanId')

        # Return an object of this model
        return cls(settings,
                   vlan_id)



# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""

import meraki.models.stp_bridge_priority_model

class UpdateNetworkSwitchSettingsStpModel(object):

    """Implementation of the 'updateNetworkSwitchSettingsStp' model.

    TODO: type model description here.

    Attributes:
        rstp_enabled (bool): The spanning tree protocol status in network
        stp_bridge_priority (list of StpBridgePriorityModel): STP bridge
            priority for switches/stacks or switch profiles. An empty array
            will clear the STP bridge priority settings.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "rstp_enabled":'rstpEnabled',
        "stp_bridge_priority":'stpBridgePriority'
    }

    def __init__(self,
                 rstp_enabled=None,
                 stp_bridge_priority=None):
        """Constructor for the UpdateNetworkSwitchSettingsStpModel class"""

        # Initialize members of the class
        self.rstp_enabled = rstp_enabled
        self.stp_bridge_priority = stp_bridge_priority


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
        rstp_enabled = dictionary.get('rstpEnabled')
        stp_bridge_priority = None
        if dictionary.get('stpBridgePriority') != None:
            stp_bridge_priority = list()
            for structure in dictionary.get('stpBridgePriority'):
                stp_bridge_priority.append(meraki.models.stp_bridge_priority_model.StpBridgePriorityModel.from_dictionary(structure))

        # Return an object of this model
        return cls(rstp_enabled,
                   stp_bridge_priority)



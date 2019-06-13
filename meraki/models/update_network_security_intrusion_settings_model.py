# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""

import meraki.models.protected_networks_model

class UpdateNetworkSecurityIntrusionSettingsModel(object):

    """Implementation of the 'updateNetworkSecurityIntrusionSettings' model.

    TODO: type model description here.

    Attributes:
        mode (string): Set mode to 'disabled'/'detection'/'prevention'
            (optional - omitting will leave current config unchanged)
        ids_rulesets (string): Set the detection ruleset
            'connectivity'/'balanced'/'security' (optional - omitting will
            leave current config unchanged). Default value is 'balanced' if
            none currently saved
        protected_networks (ProtectedNetworksModel): Set the included/excluded
            networks from the intrusion engine (optional - omitting will leave
            current config unchanged)

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "mode":'mode',
        "ids_rulesets":'idsRulesets',
        "protected_networks":'protectedNetworks'
    }

    def __init__(self,
                 mode=None,
                 ids_rulesets=None,
                 protected_networks=None):
        """Constructor for the UpdateNetworkSecurityIntrusionSettingsModel class"""

        # Initialize members of the class
        self.mode = mode
        self.ids_rulesets = ids_rulesets
        self.protected_networks = protected_networks


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
        mode = dictionary.get('mode')
        ids_rulesets = dictionary.get('idsRulesets')
        protected_networks = meraki.models.protected_networks_model.ProtectedNetworksModel.from_dictionary(dictionary.get('protectedNetworks')) if dictionary.get('protectedNetworks') else None

        # Return an object of this model
        return cls(mode,
                   ids_rulesets,
                   protected_networks)



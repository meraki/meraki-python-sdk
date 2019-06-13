# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""

import meraki.models.rule5_model

class BonjourForwardingModel(object):

    """Implementation of the 'BonjourForwarding' model.

    The Bonjour settings for your group policy. Only valid if your network has
    a wireless configuration.

    Attributes:
        settings (Settings3Enum): How Bonjour rules are applied. Can be
            'network default', 'ignore' or 'custom'.
        rules (list of Rule5Model): A list of the Bonjour forwarding rules for
            your group policy. If 'settings' is set to 'custom', at least one
            rule must be specified.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "settings":'settings',
        "rules":'rules'
    }

    def __init__(self,
                 settings=None,
                 rules=None):
        """Constructor for the BonjourForwardingModel class"""

        # Initialize members of the class
        self.settings = settings
        self.rules = rules


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
        rules = None
        if dictionary.get('rules') != None:
            rules = list()
            for structure in dictionary.get('rules'):
                rules.append(meraki.models.rule5_model.Rule5Model.from_dictionary(structure))

        # Return an object of this model
        return cls(settings,
                   rules)



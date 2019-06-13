# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""

import meraki.models.whitelisted_rule_model

class UpdateOrganizationSecurityIntrusionSettingsModel(object):

    """Implementation of the 'updateOrganizationSecurityIntrusionSettings' model.

    TODO: type model description here.

    Attributes:
        whitelisted_rules (list of WhitelistedRuleModel): Sets a list of
            specific SNORT® signatures to whitelist

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "whitelisted_rules":'whitelistedRules'
    }

    def __init__(self,
                 whitelisted_rules=None):
        """Constructor for the UpdateOrganizationSecurityIntrusionSettingsModel class"""

        # Initialize members of the class
        self.whitelisted_rules = whitelisted_rules


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
        whitelisted_rules = None
        if dictionary.get('whitelistedRules') != None:
            whitelisted_rules = list()
            for structure in dictionary.get('whitelistedRules'):
                whitelisted_rules.append(meraki.models.whitelisted_rule_model.WhitelistedRuleModel.from_dictionary(structure))

        # Return an object of this model
        return cls(whitelisted_rules)



# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class UpdateNetworkSwitchSettingsQosRulesOrderModel(object):

    """Implementation of the 'updateNetworkSwitchSettingsQosRulesOrder' model.

    TODO: type model description here.

    Attributes:
        rule_ids (list of string): A list of quality of service rule IDs
            arranged in order in which they should be processed by the
            switch.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "rule_ids":'ruleIds'
    }

    def __init__(self,
                 rule_ids=None):
        """Constructor for the UpdateNetworkSwitchSettingsQosRulesOrderModel class"""

        # Initialize members of the class
        self.rule_ids = rule_ids


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
        rule_ids = dictionary.get('ruleIds')

        # Return an object of this model
        return cls(rule_ids)



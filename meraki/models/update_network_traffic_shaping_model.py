# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""

import meraki.models.rule7_model

class UpdateNetworkTrafficShapingModel(object):

    """Implementation of the 'updateNetworkTrafficShaping' model.

    TODO: type model description here.

    Attributes:
        default_rules_enabled (bool): Whether default traffic shaping rules
            are enabled (true) or disabled (false).     There are 4 default
            rules, which can     be seen on your network's traffic shaping
            page. Note that default rules     count against the rule limit of
            8.
        rules (list of Rule7Model): An array of traffic shaping rules. Rules
            are applied in the order that     they are specified in. An empty
            list (or null) means no rules. Note that     you are allowed a
            maximum of 8 rules.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "default_rules_enabled":'defaultRulesEnabled',
        "rules":'rules'
    }

    def __init__(self,
                 default_rules_enabled=None,
                 rules=None):
        """Constructor for the UpdateNetworkTrafficShapingModel class"""

        # Initialize members of the class
        self.default_rules_enabled = default_rules_enabled
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
        default_rules_enabled = dictionary.get('defaultRulesEnabled')
        rules = None
        if dictionary.get('rules') != None:
            rules = list()
            for structure in dictionary.get('rules'):
                rules.append(meraki.models.rule7_model.Rule7Model.from_dictionary(structure))

        # Return an object of this model
        return cls(default_rules_enabled,
                   rules)



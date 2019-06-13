# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""

import meraki.models.traffic_shaping_rule_model
import meraki.models.l3_firewall_rule_model
import meraki.models.l7_firewall_rule_model

class FirewallAndTrafficShapingModel(object):

    """Implementation of the 'FirewallAndTrafficShaping' model.

    The firewall and traffic shaping rules and settings for your policy.

    Attributes:
        settings (Settings1Enum): How firewall and traffic shaping rules are
            enforced. Can be 'network default', 'ignore' or 'custom'.
        traffic_shaping_rules (list of TrafficShapingRuleModel): An array of
            traffic shaping rules. Rules are applied in the order that    
            they are specified in. An empty list (or null) means no rules.
            Note that     you are allowed a maximum of 8 rules.
        l_3_firewall_rules (list of L3FirewallRuleModel): An ordered array of
            the L3 firewall rules
        l_7_firewall_rules (list of L7FirewallRuleModel): An ordered array of
            L7 firewall rules

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "settings":'settings',
        "traffic_shaping_rules":'trafficShapingRules',
        "l3_firewall_rules":'l3FirewallRules',
        "l7_firewall_rules":'l7FirewallRules'
    }

    def __init__(self,
                 settings=None,
                 traffic_shaping_rules=None,
                 l3_firewall_rules=None,
                 l7_firewall_rules=None):
        """Constructor for the FirewallAndTrafficShapingModel class"""

        # Initialize members of the class
        self.settings = settings
        self.traffic_shaping_rules = traffic_shaping_rules
        self.l3_firewall_rules = l3_firewall_rules
        self.l7_firewall_rules = l7_firewall_rules


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
        traffic_shaping_rules = None
        if dictionary.get('trafficShapingRules') != None:
            traffic_shaping_rules = list()
            for structure in dictionary.get('trafficShapingRules'):
                traffic_shaping_rules.append(meraki.models.traffic_shaping_rule_model.TrafficShapingRuleModel.from_dictionary(structure))
        l3_firewall_rules = None
        if dictionary.get('l3FirewallRules') != None:
            l3_firewall_rules = list()
            for structure in dictionary.get('l3FirewallRules'):
                l3_firewall_rules.append(meraki.models.l3_firewall_rule_model.L3FirewallRuleModel.from_dictionary(structure))
        l7_firewall_rules = None
        if dictionary.get('l7FirewallRules') != None:
            l7_firewall_rules = list()
            for structure in dictionary.get('l7FirewallRules'):
                l7_firewall_rules.append(meraki.models.l7_firewall_rule_model.L7FirewallRuleModel.from_dictionary(structure))

        # Return an object of this model
        return cls(settings,
                   traffic_shaping_rules,
                   l3_firewall_rules,
                   l7_firewall_rules)



# -*- coding: utf-8 -*-

"""
    meraki_sdk

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""

import meraki_sdk.models.port_rule_model

class Rule7Model(object):

    """Implementation of the 'Rule7' model.

    TODO: type model description here.

    Attributes:
        public_ip (string): The IP address that will be used to access the
            internal resource from the WAN
        uplink (Uplink1Enum): The physical WAN interface on which the traffic
            will arrive ('internet1' or, if available, 'internet2')
        port_rules (list of PortRuleModel): An array of associated forwarding
            rules

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "public_ip":'publicIp',
        "uplink":'uplink',
        "port_rules":'portRules'
    }

    def __init__(self,
                 public_ip=None,
                 uplink=None,
                 port_rules=None):
        """Constructor for the Rule7Model class"""

        # Initialize members of the class
        self.public_ip = public_ip
        self.uplink = uplink
        self.port_rules = port_rules


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
        public_ip = dictionary.get('publicIp')
        uplink = dictionary.get('uplink')
        port_rules = None
        if dictionary.get('portRules') != None:
            port_rules = list()
            for structure in dictionary.get('portRules'):
                port_rules.append(meraki_sdk.models.port_rule_model.PortRuleModel.from_dictionary(structure))

        # Return an object of this model
        return cls(public_ip,
                   uplink,
                   port_rules)



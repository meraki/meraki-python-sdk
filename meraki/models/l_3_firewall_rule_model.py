# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class L3FirewallRuleModel(object):

    """Implementation of the 'L3FirewallRule' model.

    TODO: type model description here.

    Attributes:
        comment (string): Description of the rule (optional)
        policy (string): 'allow' or 'deny' traffic specified by this rule
        protocol (string): The type of protocol (must be 'tcp', 'udp', 'icmp'
            or 'any')
        dest_port (string): Destination port (integer in the range 1-65535), a
            port range (e.g. 8080-9090), or 'any'
        dest_cidr (string): Destination IP address (in IP or CIDR notation), a
            fully-qualified domain name (FQDN, if your network supports it) or
            'any'.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "policy":'policy',
        "protocol":'protocol',
        "dest_cidr":'destCidr',
        "comment":'comment',
        "dest_port":'destPort'
    }

    def __init__(self,
                 policy=None,
                 protocol=None,
                 dest_cidr=None,
                 comment=None,
                 dest_port=None):
        """Constructor for the L3FirewallRuleModel class"""

        # Initialize members of the class
        self.comment = comment
        self.policy = policy
        self.protocol = protocol
        self.dest_port = dest_port
        self.dest_cidr = dest_cidr


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
        policy = dictionary.get('policy')
        protocol = dictionary.get('protocol')
        dest_cidr = dictionary.get('destCidr')
        comment = dictionary.get('comment')
        dest_port = dictionary.get('destPort')

        # Return an object of this model
        return cls(policy,
                   protocol,
                   dest_cidr,
                   comment,
                   dest_port)



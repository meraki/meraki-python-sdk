# -*- coding: utf-8 -*-

"""
    meraki_sdk

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class Rule12Model(object):

    """Implementation of the 'Rule12' model.

    TODO: type model description here.

    Attributes:
        comment (string): Description of the rule (optional).
        policy (Policy7Enum): 'allow' or 'deny' traffic specified by this
            rule.
        ip_version (IpVersionEnum): IP address version (must be 'any', 'ipv4'
            or 'ipv6'). Applicable only if network supports IPv6. Default
            value is 'ipv4'.
        protocol (Protocol4Enum): The type of protocol (must be 'tcp', 'udp',
            or 'any').
        src_cidr (string): Source IP address (in IP or CIDR notation) or
            'any'.
        src_port (string): Source port. Must be in the range  of 1-65535 or
            'any'. Default is 'any'.
        dst_cidr (string): Destination IP address (in IP or CIDR notation) or
            'any'.
        dst_port (string): Destination port. Must be in the range of 1-65535
            or 'any'. Default is 'any'.
        vlan (string): Incoming traffic VLAN. Must be in the range of 1-4095
            or 'any'. Default is 'any'.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "policy":'policy',
        "protocol":'protocol',
        "src_cidr":'srcCidr',
        "dst_cidr":'dstCidr',
        "comment":'comment',
        "ip_version":'ipVersion',
        "src_port":'srcPort',
        "dst_port":'dstPort',
        "vlan":'vlan'
    }

    def __init__(self,
                 policy=None,
                 protocol=None,
                 src_cidr=None,
                 dst_cidr=None,
                 comment=None,
                 ip_version=None,
                 src_port=None,
                 dst_port=None,
                 vlan=None):
        """Constructor for the Rule12Model class"""

        # Initialize members of the class
        self.comment = comment
        self.policy = policy
        self.ip_version = ip_version
        self.protocol = protocol
        self.src_cidr = src_cidr
        self.src_port = src_port
        self.dst_cidr = dst_cidr
        self.dst_port = dst_port
        self.vlan = vlan


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
        src_cidr = dictionary.get('srcCidr')
        dst_cidr = dictionary.get('dstCidr')
        comment = dictionary.get('comment')
        ip_version = dictionary.get('ipVersion')
        src_port = dictionary.get('srcPort')
        dst_port = dictionary.get('dstPort')
        vlan = dictionary.get('vlan')

        # Return an object of this model
        return cls(policy,
                   protocol,
                   src_cidr,
                   dst_cidr,
                   comment,
                   ip_version,
                   src_port,
                   dst_port,
                   vlan)



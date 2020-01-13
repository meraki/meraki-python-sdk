# -*- coding: utf-8 -*-

"""
    meraki_sdk

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class RuleModel(object):

    """Implementation of the 'Rule' model.

    TODO: type model description here.

    Attributes:
        name (string): A descriptive name for the rule
        lan_ip (string): The IP address of the server or device that hosts the
            internal resource that you wish to make available on the WAN
        public_port (string): A port or port ranges that will be forwarded to
            the host on the LAN
        local_port (string): A port or port ranges that will receive the
            forwarded traffic from the WAN
        allowed_ips (list of string): An array of ranges of WAN IP addresses
            that are allowed to make inbound connections on the specified
            ports or port ranges.
        protocol (string): TCP or UDP
        access (string): `any` or `restricted`. Specify the right to make
            inbound connections on the specified ports or port ranges. If
            `restricted`, a list of allowed IPs is mandatory.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "lan_ip":'lanIp',
        "public_port":'publicPort',
        "local_port":'localPort',
        "protocol":'protocol',
        "access":'access',
        "name":'name',
        "allowed_ips":'allowedIps'
    }

    def __init__(self,
                 lan_ip=None,
                 public_port=None,
                 local_port=None,
                 protocol=None,
                 access=None,
                 name=None,
                 allowed_ips=None):
        """Constructor for the RuleModel class"""

        # Initialize members of the class
        self.name = name
        self.lan_ip = lan_ip
        self.public_port = public_port
        self.local_port = local_port
        self.allowed_ips = allowed_ips
        self.protocol = protocol
        self.access = access


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
        lan_ip = dictionary.get('lanIp')
        public_port = dictionary.get('publicPort')
        local_port = dictionary.get('localPort')
        protocol = dictionary.get('protocol')
        access = dictionary.get('access')
        name = dictionary.get('name')
        allowed_ips = dictionary.get('allowedIps')

        # Return an object of this model
        return cls(lan_ip,
                   public_port,
                   local_port,
                   protocol,
                   access,
                   name,
                   allowed_ips)



# -*- coding: utf-8 -*-

"""
    meraki_sdk

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class PortRuleModel(object):

    """Implementation of the 'PortRule' model.

    TODO: type model description here.

    Attributes:
        name (string): A description of the rule
        protocol (Protocol3Enum): 'tcp' or 'udp'
        public_port (string): Destination port of the traffic that is arriving
            on the WAN
        local_ip (string): Local IP address to which traffic will be
            forwarded
        local_port (string): Destination port of the forwarded traffic that
            will be sent from the MX to the specified host on the LAN. If you
            simply wish to forward the traffic without translating the port,
            this should be the same as the Public port
        allowed_ips (list of string): Remote IP addresses or ranges that are
            permitted to access the internal resource via this port forwarding
            rule, or 'any'

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name":'name',
        "protocol":'protocol',
        "public_port":'publicPort',
        "local_ip":'localIp',
        "local_port":'localPort',
        "allowed_ips":'allowedIps'
    }

    def __init__(self,
                 name=None,
                 protocol=None,
                 public_port=None,
                 local_ip=None,
                 local_port=None,
                 allowed_ips=None):
        """Constructor for the PortRuleModel class"""

        # Initialize members of the class
        self.name = name
        self.protocol = protocol
        self.public_port = public_port
        self.local_ip = local_ip
        self.local_port = local_port
        self.allowed_ips = allowed_ips


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
        name = dictionary.get('name')
        protocol = dictionary.get('protocol')
        public_port = dictionary.get('publicPort')
        local_ip = dictionary.get('localIp')
        local_port = dictionary.get('localPort')
        allowed_ips = dictionary.get('allowedIps')

        # Return an object of this model
        return cls(name,
                   protocol,
                   public_port,
                   local_ip,
                   local_port,
                   allowed_ips)



# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class Wan2Model(object):

    """Implementation of the 'Wan2' model.

    WAN 2 settings (only for MX devices)

    Attributes:
        wan_enabled (WanEnabledEnum): Enable or disable the interface (only
            for MX devices). Valid values are 'enabled', 'disabled', and 'not
            configured'.
        using_static_ip (bool): Configue the interface to have static IP
            settings or use DHCP.
        static_ip (string): The IP the device should use on the WAN.
        static_gateway_ip (string): The IP of the gateway on the WAN.
        static_subnet_mask (string): The subnet mask for the WAN.
        static_dns (list of string): Up to two DNS IPs.
        vlan (int): The VLAN that management traffic should be tagged with.
            Applies whether usingStaticIp is true or false.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "wan_enabled":'wanEnabled',
        "using_static_ip":'usingStaticIp',
        "static_ip":'staticIp',
        "static_gateway_ip":'staticGatewayIp',
        "static_subnet_mask":'staticSubnetMask',
        "static_dns":'staticDns',
        "vlan":'vlan'
    }

    def __init__(self,
                 wan_enabled=None,
                 using_static_ip=None,
                 static_ip=None,
                 static_gateway_ip=None,
                 static_subnet_mask=None,
                 static_dns=None,
                 vlan=None):
        """Constructor for the Wan2Model class"""

        # Initialize members of the class
        self.wan_enabled = wan_enabled
        self.using_static_ip = using_static_ip
        self.static_ip = static_ip
        self.static_gateway_ip = static_gateway_ip
        self.static_subnet_mask = static_subnet_mask
        self.static_dns = static_dns
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
        wan_enabled = dictionary.get('wanEnabled')
        using_static_ip = dictionary.get('usingStaticIp')
        static_ip = dictionary.get('staticIp')
        static_gateway_ip = dictionary.get('staticGatewayIp')
        static_subnet_mask = dictionary.get('staticSubnetMask')
        static_dns = dictionary.get('staticDns')
        vlan = dictionary.get('vlan')

        # Return an object of this model
        return cls(wan_enabled,
                   using_static_ip,
                   static_ip,
                   static_gateway_ip,
                   static_subnet_mask,
                   static_dns,
                   vlan)



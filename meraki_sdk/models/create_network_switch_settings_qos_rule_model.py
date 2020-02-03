# -*- coding: utf-8 -*-

"""
    meraki_sdk

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class CreateNetworkSwitchSettingsQosRuleModel(object):

    """Implementation of the 'createNetworkSwitchSettingsQosRule' model.

    TODO: type model description here.

    Attributes:
        vlan (int): The VLAN of the incoming packet. A null value will match
            any VLAN.
        protocol (Protocol6Enum): The protocol of the incoming packet. Can be
            one of "ANY", "TCP" or "UDP". Default value is "ANY"
        src_port (int): The source port of the incoming packet. Applicable
            only if protocol is TCP or UDP.
        src_port_range (string): The source port range of the incoming packet.
            Applicable only if protocol is set to TCP or UDP. Example: 70-80
        dst_port (int): The destination port of the incoming packet.
            Applicable only if protocol is TCP or UDP.
        dst_port_range (string): The destination port range of the incoming
            packet. Applicable only if protocol is set to TCP or UDP. Example:
            70-80
        dscp (int): DSCP tag. Set this to -1 to trust incoming DSCP. Default
            value is 0

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "vlan":'vlan',
        "protocol":'protocol',
        "src_port":'srcPort',
        "src_port_range":'srcPortRange',
        "dst_port":'dstPort',
        "dst_port_range":'dstPortRange',
        "dscp":'dscp'
    }

    def __init__(self,
                 vlan=None,
                 protocol=None,
                 src_port=None,
                 src_port_range=None,
                 dst_port=None,
                 dst_port_range=None,
                 dscp=None):
        """Constructor for the CreateNetworkSwitchSettingsQosRuleModel class"""

        # Initialize members of the class
        self.vlan = vlan
        self.protocol = protocol
        self.src_port = src_port
        self.src_port_range = src_port_range
        self.dst_port = dst_port
        self.dst_port_range = dst_port_range
        self.dscp = dscp


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
        vlan = dictionary.get('vlan')
        protocol = dictionary.get('protocol')
        src_port = dictionary.get('srcPort')
        src_port_range = dictionary.get('srcPortRange')
        dst_port = dictionary.get('dstPort')
        dst_port_range = dictionary.get('dstPortRange')
        dscp = dictionary.get('dscp')

        # Return an object of this model
        return cls(vlan,
                   protocol,
                   src_port,
                   src_port_range,
                   dst_port,
                   dst_port_range,
                   dscp)



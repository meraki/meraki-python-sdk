# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class UpdateNetworkAppliancePortModel(object):

    """Implementation of the 'updateNetworkAppliancePort' model.

    TODO: type model description here.

    Attributes:
        enabled (bool): The status of the port
        drop_untagged_traffic (bool): Trunk port can Drop all Untagged
            traffic. When true, no VLAN is required. Access ports cannot have
            dropUntaggedTraffic set to true.
        mtype (string): The type of the port: 'access' or 'trunk'.
        vlan (int): Native VLAN when the port is in Trunk mode. Access VLAN
            when the port is in Access mode.
        allowed_vlans (string): Comma-delimited list of the VLAN ID's allowed
            on the port, or 'all' to permit all VLAN's on the port.
        access_policy (string): The name of the policy. Only applicable to
            Access ports. Valid values are: 'open', '8021x-radius',
            'mac-radius', 'hybris-radius' for MX64 or Z3 or any MX supporting
            the per port authentication feature. Otherwise, 'open' is the only
            valid value and 'open' is the default value if the field is
            missing.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "enabled":'enabled',
        "drop_untagged_traffic":'dropUntaggedTraffic',
        "mtype":'type',
        "vlan":'vlan',
        "allowed_vlans":'allowedVlans',
        "access_policy":'accessPolicy'
    }

    def __init__(self,
                 enabled=None,
                 drop_untagged_traffic=None,
                 mtype=None,
                 vlan=None,
                 allowed_vlans=None,
                 access_policy=None):
        """Constructor for the UpdateNetworkAppliancePortModel class"""

        # Initialize members of the class
        self.enabled = enabled
        self.drop_untagged_traffic = drop_untagged_traffic
        self.mtype = mtype
        self.vlan = vlan
        self.allowed_vlans = allowed_vlans
        self.access_policy = access_policy


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
        enabled = dictionary.get('enabled')
        drop_untagged_traffic = dictionary.get('dropUntaggedTraffic')
        mtype = dictionary.get('type')
        vlan = dictionary.get('vlan')
        allowed_vlans = dictionary.get('allowedVlans')
        access_policy = dictionary.get('accessPolicy')

        # Return an object of this model
        return cls(enabled,
                   drop_untagged_traffic,
                   mtype,
                   vlan,
                   allowed_vlans,
                   access_policy)



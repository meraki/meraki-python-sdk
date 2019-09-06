# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class UpdateNetworkWarmSpareSettingsModel(object):

    """Implementation of the 'updateNetworkWarmSpareSettings' model.

    TODO: type model description here.

    Attributes:
        enabled (bool): Enable warm spare
        spare_serial (string): Serial number of the warm spare appliance
        uplink_mode (string): Uplink mode, either virtual or public
        virtual_ip_1 (string): The WAN 1 shared IP
        virtual_ip_2 (string): The WAN 2 shared IP

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "enabled":'enabled',
        "spare_serial":'spareSerial',
        "uplink_mode":'uplinkMode',
        "virtual_ip1":'virtualIp1',
        "virtual_ip2":'virtualIp2'
    }

    def __init__(self,
                 enabled=None,
                 spare_serial=None,
                 uplink_mode=None,
                 virtual_ip1=None,
                 virtual_ip2=None):
        """Constructor for the UpdateNetworkWarmSpareSettingsModel class"""

        # Initialize members of the class
        self.enabled = enabled
        self.spare_serial = spare_serial
        self.uplink_mode = uplink_mode
        self.virtual_ip1 = virtual_ip1
        self.virtual_ip2 = virtual_ip2


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
        spare_serial = dictionary.get('spareSerial')
        uplink_mode = dictionary.get('uplinkMode')
        virtual_ip1 = dictionary.get('virtualIp1')
        virtual_ip2 = dictionary.get('virtualIp2')

        # Return an object of this model
        return cls(enabled,
                   spare_serial,
                   uplink_mode,
                   virtual_ip1,
                   virtual_ip2)



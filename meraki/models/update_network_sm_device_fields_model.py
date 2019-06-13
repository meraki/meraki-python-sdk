# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""

import meraki.models.device_fields_model

class UpdateNetworkSmDeviceFieldsModel(object):

    """Implementation of the 'updateNetworkSmDeviceFields' model.

    TODO: type model description here.

    Attributes:
        wifi_mac (string): The wifiMac of the device to be modified.
        id (string): The id of the device to be modified.
        serial (string): The serial of the device to be modified.
        device_fields (DeviceFieldsModel): The new fields of the device. Each
            field of this object is optional.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "device_fields":'deviceFields',
        "wifi_mac":'wifiMac',
        "id":'id',
        "serial":'serial'
    }

    def __init__(self,
                 device_fields=None,
                 wifi_mac=None,
                 id=None,
                 serial=None):
        """Constructor for the UpdateNetworkSmDeviceFieldsModel class"""

        # Initialize members of the class
        self.wifi_mac = wifi_mac
        self.id = id
        self.serial = serial
        self.device_fields = device_fields


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
        device_fields = meraki.models.device_fields_model.DeviceFieldsModel.from_dictionary(dictionary.get('deviceFields')) if dictionary.get('deviceFields') else None
        wifi_mac = dictionary.get('wifiMac')
        id = dictionary.get('id')
        serial = dictionary.get('serial')

        # Return an object of this model
        return cls(device_fields,
                   wifi_mac,
                   id,
                   serial)



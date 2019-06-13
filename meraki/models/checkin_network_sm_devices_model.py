# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class CheckinNetworkSmDevicesModel(object):

    """Implementation of the 'checkinNetworkSmDevices' model.

    TODO: type model description here.

    Attributes:
        wifi_macs (string): The wifiMacs of the devices to be checked-in.
        ids (string): The ids of the devices to be checked-in.
        serials (string): The serials of the devices to be checked-in.
        scope (string): The scope (one of all, none, withAny, withAll,
            withoutAny, or withoutAll) and a set of tags of the devices to be
            checked-in.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "wifi_macs":'wifiMacs',
        "ids":'ids',
        "serials":'serials',
        "scope":'scope'
    }

    def __init__(self,
                 wifi_macs=None,
                 ids=None,
                 serials=None,
                 scope=None):
        """Constructor for the CheckinNetworkSmDevicesModel class"""

        # Initialize members of the class
        self.wifi_macs = wifi_macs
        self.ids = ids
        self.serials = serials
        self.scope = scope


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
        wifi_macs = dictionary.get('wifiMacs')
        ids = dictionary.get('ids')
        serials = dictionary.get('serials')
        scope = dictionary.get('scope')

        # Return an object of this model
        return cls(wifi_macs,
                   ids,
                   serials,
                   scope)



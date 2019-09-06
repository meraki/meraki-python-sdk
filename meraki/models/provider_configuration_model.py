# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class ProviderConfigurationModel(object):

    """Implementation of the 'ProviderConfiguration' model.

    TODO: type model description here.

    Attributes:
        key (string): The key for an object in ProviderConfiguration
        mtype (string): The type for an object in ProviderConfiguration. Can
            be one of 'manual_string', 'manual_int', 'manual_boolean',
            'manual_choice', 'manual_multiselect', 'manual_list',
            'auto_username', 'auto_email', 'auto_mac_address',
            'auto_serial_number', 'auto_notes' or 'auto_name'
        value (string): The value for an object in ProviderConfiguration

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "key":'key',
        "mtype":'type',
        "value":'value'
    }

    def __init__(self,
                 key=None,
                 mtype=None,
                 value=None):
        """Constructor for the ProviderConfigurationModel class"""

        # Initialize members of the class
        self.key = key
        self.mtype = mtype
        self.value = value


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
        key = dictionary.get('key')
        mtype = dictionary.get('type')
        value = dictionary.get('value')

        # Return an object of this model
        return cls(key,
                   mtype,
                   value)



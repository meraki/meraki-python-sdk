# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class PowerExceptionModel(object):

    """Implementation of the 'PowerException' model.

    TODO: type model description here.

    Attributes:
        serial (string): Serial number of the switch
        power_type (PowerTypeEnum): Per switch exception (combined, redundant,
            useNetworkSetting)

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "serial":'serial',
        "power_type":'powerType'
    }

    def __init__(self,
                 serial=None,
                 power_type=None):
        """Constructor for the PowerExceptionModel class"""

        # Initialize members of the class
        self.serial = serial
        self.power_type = power_type


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
        serial = dictionary.get('serial')
        power_type = dictionary.get('powerType')

        # Return an object of this model
        return cls(serial,
                   power_type)



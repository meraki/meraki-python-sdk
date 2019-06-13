# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class RemoveNetworkSwitchStackModel(object):

    """Implementation of the 'removeNetworkSwitchStack' model.

    TODO: type model description here.

    Attributes:
        serial (string): The serial of the switch to be removed

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "serial":'serial'
    }

    def __init__(self,
                 serial=None):
        """Constructor for the RemoveNetworkSwitchStackModel class"""

        # Initialize members of the class
        self.serial = serial


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

        # Return an object of this model
        return cls(serial)



# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class DeviceFieldsModel(object):

    """Implementation of the 'DeviceFields' model.

    The new fields of the device. Each field of this object is optional.

    Attributes:
        name (string): New name for the device
        notes (string): New notes for the device

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name":'name',
        "notes":'notes'
    }

    def __init__(self,
                 name=None,
                 notes=None):
        """Constructor for the DeviceFieldsModel class"""

        # Initialize members of the class
        self.name = name
        self.notes = notes


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
        notes = dictionary.get('notes')

        # Return an object of this model
        return cls(name,
                   notes)



# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class DestinationModel(object):

    """Implementation of the 'Destination' model.

    TODO: type model description here.

    Attributes:
        ip (string): The IP address to test connectivity with
        description (string): Description of the testing destination.
            Optional, defaults to null
        default (bool): Boolean indicating whether this is the default testing
            destination (true) or not (false). Defaults to false. Only one
            default is allowed

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "ip":'ip',
        "description":'description',
        "default":'default'
    }

    def __init__(self,
                 ip=None,
                 description=None,
                 default=None):
        """Constructor for the DestinationModel class"""

        # Initialize members of the class
        self.ip = ip
        self.description = description
        self.default = default


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
        ip = dictionary.get('ip')
        description = dictionary.get('description')
        default = dictionary.get('default')

        # Return an object of this model
        return cls(ip,
                   description,
                   default)



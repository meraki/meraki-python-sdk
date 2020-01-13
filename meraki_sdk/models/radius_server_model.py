# -*- coding: utf-8 -*-

"""
    meraki_sdk

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class RadiusServerModel(object):

    """Implementation of the 'RadiusServer' model.

    TODO: type model description here.

    Attributes:
        host (string): IP address of your RADIUS server
        port (int): UDP port the RADIUS server listens on for Access-requests
        secret (string): RADIUS client shared secret

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "host":'host',
        "secret":'secret',
        "port":'port'
    }

    def __init__(self,
                 host=None,
                 secret=None,
                 port=None):
        """Constructor for the RadiusServerModel class"""

        # Initialize members of the class
        self.host = host
        self.port = port
        self.secret = secret


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
        host = dictionary.get('host')
        secret = dictionary.get('secret')
        port = dictionary.get('port')

        # Return an object of this model
        return cls(host,
                   secret,
                   port)



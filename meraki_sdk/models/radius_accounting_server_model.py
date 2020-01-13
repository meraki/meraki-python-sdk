# -*- coding: utf-8 -*-

"""
    meraki_sdk

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class RadiusAccountingServerModel(object):

    """Implementation of the 'RadiusAccountingServer' model.

    TODO: type model description here.

    Attributes:
        host (string): IP address to which the APs will send RADIUS accounting
            messages
        port (int): Port on the RADIUS server that is listening for accounting
            messages
        secret (string): Shared key used to authenticate messages between the
            APs and RADIUS server

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
        """Constructor for the RadiusAccountingServerModel class"""

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



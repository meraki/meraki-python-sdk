# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class DefinitionModel(object):

    """Implementation of the 'Definition' model.

    TODO: type model description here.

    Attributes:
        mtype (Type1Enum): The type of definition. Can be one of
            'application', 'applicationCategory', 'host', 'port', 'ipRange' or
            'localNet'.
        value (string): If "type" is 'host', 'port', 'ipRange' or 'localNet',
            then "value" must be a string, matching either     a hostname
            (e.g. "somesite.com"), a port (e.g. 8080), or an IP range
            ("192.1.0.0",     "192.1.0.0/16", or "10.1.0.0/16:80"). 'localNet'
            also supports CIDR notation, excluding     custom ports.      If
            "type" is 'application' or 'applicationCategory', then "value"
            must be an object     with the structure { "id":
            "meraki:layer7/..." }, where "id" is the application category or  
            application ID (for a list of IDs for your network, use the
            trafficShaping/applicationCategories     endpoint).

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "mtype":'type',
        "value":'value'
    }

    def __init__(self,
                 mtype=None,
                 value=None):
        """Constructor for the DefinitionModel class"""

        # Initialize members of the class
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
        mtype = dictionary.get('type')
        value = dictionary.get('value')

        # Return an object of this model
        return cls(mtype,
                   value)



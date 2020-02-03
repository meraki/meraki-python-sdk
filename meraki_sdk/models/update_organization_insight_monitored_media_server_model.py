# -*- coding: utf-8 -*-

"""
    meraki_sdk

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class UpdateOrganizationInsightMonitoredMediaServerModel(object):

    """Implementation of the 'updateOrganizationInsightMonitoredMediaServer' model.

    TODO: type model description here.

    Attributes:
        name (string): The name of the VoIP provider
        address (string): The IP address (IPv4 only) or hostname of the media
            server to monitor

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name":'name',
        "address":'address'
    }

    def __init__(self,
                 name=None,
                 address=None):
        """Constructor for the UpdateOrganizationInsightMonitoredMediaServerModel class"""

        # Initialize members of the class
        self.name = name
        self.address = address


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
        address = dictionary.get('address')

        # Return an object of this model
        return cls(name,
                   address)



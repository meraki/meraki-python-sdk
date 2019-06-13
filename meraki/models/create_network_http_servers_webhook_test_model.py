# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class CreateNetworkHttpServersWebhookTestModel(object):

    """Implementation of the 'createNetworkHttpServersWebhookTest' model.

    TODO: type model description here.

    Attributes:
        url (string): The URL where the test webhook will be sent

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "url":'url'
    }

    def __init__(self,
                 url=None):
        """Constructor for the CreateNetworkHttpServersWebhookTestModel class"""

        # Initialize members of the class
        self.url = url


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
        url = dictionary.get('url')

        # Return an object of this model
        return cls(url)



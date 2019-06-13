# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class AllowedUrlModel(object):

    """Implementation of the 'AllowedUrl' model.

    TODO: type model description here.

    Attributes:
        url (string): The url to whitelist
        comment (string): Comment about the whitelisted entity

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "url":'url',
        "comment":'comment'
    }

    def __init__(self,
                 url=None,
                 comment=None):
        """Constructor for the AllowedUrlModel class"""

        # Initialize members of the class
        self.url = url
        self.comment = comment


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
        comment = dictionary.get('comment')

        # Return an object of this model
        return cls(url,
                   comment)



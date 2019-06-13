# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class AllowedFileModel(object):

    """Implementation of the 'AllowedFile' model.

    TODO: type model description here.

    Attributes:
        sha_256 (string): The file sha256 hash to whitelist
        comment (string): Comment about the whitelisted entity

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "sha256":'sha256',
        "comment":'comment'
    }

    def __init__(self,
                 sha256=None,
                 comment=None):
        """Constructor for the AllowedFileModel class"""

        # Initialize members of the class
        self.sha256 = sha256
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
        sha256 = dictionary.get('sha256')
        comment = dictionary.get('comment')

        # Return an object of this model
        return cls(sha256,
                   comment)



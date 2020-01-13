# -*- coding: utf-8 -*-

"""
    meraki_sdk

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class AllowedUrlPatternsModel(object):

    """Implementation of the 'AllowedUrlPatterns' model.

    Settings for whitelisted URL patterns

    Attributes:
        settings (Settings2Enum): How URL patterns are applied. Can be
            'network default', 'append' or 'override'.
        patterns (list of string): A whitelist of URL patterns to allow

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "settings":'settings',
        "patterns":'patterns'
    }

    def __init__(self,
                 settings=None,
                 patterns=None):
        """Constructor for the AllowedUrlPatternsModel class"""

        # Initialize members of the class
        self.settings = settings
        self.patterns = patterns


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
        settings = dictionary.get('settings')
        patterns = dictionary.get('patterns')

        # Return an object of this model
        return cls(settings,
                   patterns)



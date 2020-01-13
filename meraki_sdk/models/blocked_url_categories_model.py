# -*- coding: utf-8 -*-

"""
    meraki_sdk

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class BlockedUrlCategoriesModel(object):

    """Implementation of the 'BlockedUrlCategories' model.

    Settings for blacklisted URL categories

    Attributes:
        settings (Settings4Enum): How URL categories are applied. Can be
            'network default', 'append' or 'override'.
        categories (list of string): A list of URL categories to block

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "settings":'settings',
        "categories":'categories'
    }

    def __init__(self,
                 settings=None,
                 categories=None):
        """Constructor for the BlockedUrlCategoriesModel class"""

        # Initialize members of the class
        self.settings = settings
        self.categories = categories


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
        categories = dictionary.get('categories')

        # Return an object of this model
        return cls(settings,
                   categories)



# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""

import meraki.models.allowed_url_patterns_model
import meraki.models.blocked_url_patterns_model
import meraki.models.blocked_url_categories_model

class ContentFilteringModel(object):

    """Implementation of the 'ContentFiltering' model.

    The content filtering settings for your group policy

    Attributes:
        allowed_url_patterns (AllowedUrlPatternsModel): Settings for
            whitelisted URL patterns
        blocked_url_patterns (BlockedUrlPatternsModel): Settings for
            blacklisted URL patterns
        blocked_url_categories (BlockedUrlCategoriesModel): Settings for
            blacklisted URL categories

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "allowed_url_patterns":'allowedUrlPatterns',
        "blocked_url_patterns":'blockedUrlPatterns',
        "blocked_url_categories":'blockedUrlCategories'
    }

    def __init__(self,
                 allowed_url_patterns=None,
                 blocked_url_patterns=None,
                 blocked_url_categories=None):
        """Constructor for the ContentFilteringModel class"""

        # Initialize members of the class
        self.allowed_url_patterns = allowed_url_patterns
        self.blocked_url_patterns = blocked_url_patterns
        self.blocked_url_categories = blocked_url_categories


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
        allowed_url_patterns = meraki.models.allowed_url_patterns_model.AllowedUrlPatternsModel.from_dictionary(dictionary.get('allowedUrlPatterns')) if dictionary.get('allowedUrlPatterns') else None
        blocked_url_patterns = meraki.models.blocked_url_patterns_model.BlockedUrlPatternsModel.from_dictionary(dictionary.get('blockedUrlPatterns')) if dictionary.get('blockedUrlPatterns') else None
        blocked_url_categories = meraki.models.blocked_url_categories_model.BlockedUrlCategoriesModel.from_dictionary(dictionary.get('blockedUrlCategories')) if dictionary.get('blockedUrlCategories') else None

        # Return an object of this model
        return cls(allowed_url_patterns,
                   blocked_url_patterns,
                   blocked_url_categories)



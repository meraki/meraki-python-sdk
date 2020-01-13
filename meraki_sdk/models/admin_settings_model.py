# -*- coding: utf-8 -*-

"""
    meraki_sdk

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class AdminSettingsModel(object):

    """Implementation of the 'AdminSettings' model.

    Settings for describing which kinds of admins this policy applies to.

    Attributes:
        applies_to (AppliesToEnum): Which kinds of admins this policy applies
            to. Can be one of 'All organization admins', 'All enterprise
            admins', 'All network admins', 'All admins of networks...', 'All
            admins of networks tagged...', 'Specific admins...', 'All admins'
            or 'All SAML admins'.
        values (list of string): If 'appliesTo' is set to one of 'Specific
            admins...', 'All admins of networks...' or 'All admins of networks
            tagged...', then you must specify this 'values' property to
            provide the set of     entities to apply the branding policy to.
            For 'Specific admins...', specify an array of admin IDs. For 'All
            admins of     networks...', specify an array of network IDs and/or
            configuration template IDs. For 'All admins of networks
            tagged...',     specify an array of tag names.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "applies_to":'appliesTo',
        "values":'values'
    }

    def __init__(self,
                 applies_to=None,
                 values=None):
        """Constructor for the AdminSettingsModel class"""

        # Initialize members of the class
        self.applies_to = applies_to
        self.values = values


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
        applies_to = dictionary.get('appliesTo')
        values = dictionary.get('values')

        # Return an object of this model
        return cls(applies_to,
                   values)



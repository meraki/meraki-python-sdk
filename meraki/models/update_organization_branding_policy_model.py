# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""

import meraki.models.admin_settings_model
import meraki.models.help_settings_1_model

class UpdateOrganizationBrandingPolicyModel(object):

    """Implementation of the 'updateOrganizationBrandingPolicy' model.

    TODO: type model description here.

    Attributes:
        name (string): Name of the Dashboard branding policy.
        enabled (bool): Boolean indicating whether this policy is enabled.
        admin_settings (AdminSettingsModel): Settings for describing which
            kinds of admins this policy applies to.
        help_settings (HelpSettings1Model): Settings for describing the
            modifications to various Help page features. Each property in this
            object accepts one of     'default or inherit' (do not modify
            functionality), 'hide' (remove the section from Dashboard), or
            'show' (always show     the section on Dashboard). Some properties
            in this object also accept custom HTML used to replace the section
            on     Dashboard; see the documentation for each property to see
            the allowed values.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name":'name',
        "enabled":'enabled',
        "admin_settings":'adminSettings',
        "help_settings":'helpSettings'
    }

    def __init__(self,
                 name=None,
                 enabled=None,
                 admin_settings=None,
                 help_settings=None):
        """Constructor for the UpdateOrganizationBrandingPolicyModel class"""

        # Initialize members of the class
        self.name = name
        self.enabled = enabled
        self.admin_settings = admin_settings
        self.help_settings = help_settings


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
        enabled = dictionary.get('enabled')
        admin_settings = meraki.models.admin_settings_model.AdminSettingsModel.from_dictionary(dictionary.get('adminSettings')) if dictionary.get('adminSettings') else None
        help_settings = meraki.models.help_settings_1_model.HelpSettings1Model.from_dictionary(dictionary.get('helpSettings')) if dictionary.get('helpSettings') else None

        # Return an object of this model
        return cls(name,
                   enabled,
                   admin_settings,
                   help_settings)



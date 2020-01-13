# -*- coding: utf-8 -*-

"""
    meraki_sdk

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class UpdateOrganizationBrandingPoliciesPrioritiesModel(object):

    """Implementation of the 'updateOrganizationBrandingPoliciesPriorities' model.

    TODO: type model description here.

    Attributes:
        branding_policy_ids (list of string): A list of branding policy IDs
            arranged in ascending priority order (IDs later in the array have
            higher priority).

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "branding_policy_ids":'brandingPolicyIds'
    }

    def __init__(self,
                 branding_policy_ids=None):
        """Constructor for the UpdateOrganizationBrandingPoliciesPrioritiesModel class"""

        # Initialize members of the class
        self.branding_policy_ids = branding_policy_ids


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
        branding_policy_ids = dictionary.get('brandingPolicyIds')

        # Return an object of this model
        return cls(branding_policy_ids)



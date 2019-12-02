# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class MoveOrganizationLicensesModel(object):

    """Implementation of the 'moveOrganizationLicenses' model.

    TODO: type model description here.

    Attributes:
        dest_organization_id (string): The ID of the organization to move the
            licenses to
        license_ids (list of string): A list of IDs of licenses to move to the
            new organization

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "dest_organization_id":'destOrganizationId',
        "license_ids":'licenseIds'
    }

    def __init__(self,
                 dest_organization_id=None,
                 license_ids=None):
        """Constructor for the MoveOrganizationLicensesModel class"""

        # Initialize members of the class
        self.dest_organization_id = dest_organization_id
        self.license_ids = license_ids


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
        dest_organization_id = dictionary.get('destOrganizationId')
        license_ids = dictionary.get('licenseIds')

        # Return an object of this model
        return cls(dest_organization_id,
                   license_ids)



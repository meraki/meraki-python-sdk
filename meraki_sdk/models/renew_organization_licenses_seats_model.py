# -*- coding: utf-8 -*-

"""
    meraki_sdk

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class RenewOrganizationLicensesSeatsModel(object):

    """Implementation of the 'renewOrganizationLicensesSeats' model.

    TODO: type model description here.

    Attributes:
        license_id_to_renew (string): The ID of the SM license to renew. This
            license must already be assigned to an SM network
        unused_license_id (string): The SM license to use to renew the seats
            on 'licenseIdToRenew'. This license must have at least as many
            seats available as there are seats on 'licenseIdToRenew'

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "license_id_to_renew":'licenseIdToRenew',
        "unused_license_id":'unusedLicenseId'
    }

    def __init__(self,
                 license_id_to_renew=None,
                 unused_license_id=None):
        """Constructor for the RenewOrganizationLicensesSeatsModel class"""

        # Initialize members of the class
        self.license_id_to_renew = license_id_to_renew
        self.unused_license_id = unused_license_id


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
        license_id_to_renew = dictionary.get('licenseIdToRenew')
        unused_license_id = dictionary.get('unusedLicenseId')

        # Return an object of this model
        return cls(license_id_to_renew,
                   unused_license_id)



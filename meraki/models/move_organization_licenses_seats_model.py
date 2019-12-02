# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class MoveOrganizationLicensesSeatsModel(object):

    """Implementation of the 'moveOrganizationLicensesSeats' model.

    TODO: type model description here.

    Attributes:
        dest_organization_id (string): The ID of the organization to move the
            SM seats to
        license_id (string): The ID of the SM license to move the seats from
        seat_count (int): The number of seats to move to the new organization.
            Must be less than or equal to the total number of seats of the
            license

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "dest_organization_id":'destOrganizationId',
        "license_id":'licenseId',
        "seat_count":'seatCount'
    }

    def __init__(self,
                 dest_organization_id=None,
                 license_id=None,
                 seat_count=None):
        """Constructor for the MoveOrganizationLicensesSeatsModel class"""

        # Initialize members of the class
        self.dest_organization_id = dest_organization_id
        self.license_id = license_id
        self.seat_count = seat_count


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
        license_id = dictionary.get('licenseId')
        seat_count = dictionary.get('seatCount')

        # Return an object of this model
        return cls(dest_organization_id,
                   license_id,
                   seat_count)



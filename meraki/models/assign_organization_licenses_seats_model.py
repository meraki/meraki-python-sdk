# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class AssignOrganizationLicensesSeatsModel(object):

    """Implementation of the 'assignOrganizationLicensesSeats' model.

    TODO: type model description here.

    Attributes:
        license_id (string): The ID of the SM license to assign seats from
        network_id (string): The ID of the SM network to assign the seats to
        seat_count (int): The number of seats to assign to the SM network.
            Must be less than or equal to the total number of seats of the
            license

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "license_id":'licenseId',
        "network_id":'networkId',
        "seat_count":'seatCount'
    }

    def __init__(self,
                 license_id=None,
                 network_id=None,
                 seat_count=None):
        """Constructor for the AssignOrganizationLicensesSeatsModel class"""

        # Initialize members of the class
        self.license_id = license_id
        self.network_id = network_id
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
        license_id = dictionary.get('licenseId')
        network_id = dictionary.get('networkId')
        seat_count = dictionary.get('seatCount')

        # Return an object of this model
        return cls(license_id,
                   network_id,
                   seat_count)



# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class UpdateOrganizationLicenseModel(object):

    """Implementation of the 'updateOrganizationLicense' model.

    TODO: type model description here.

    Attributes:
        device_serial (string): The serial number of the device to assign this
            license to. Set this to null to unassign the license. If a
            different license is already active on the device, this parameter
            will control queueing/dequeuing this license.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "device_serial":'deviceSerial'
    }

    def __init__(self,
                 device_serial=None):
        """Constructor for the UpdateOrganizationLicenseModel class"""

        # Initialize members of the class
        self.device_serial = device_serial


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
        device_serial = dictionary.get('deviceSerial')

        # Return an object of this model
        return cls(device_serial)



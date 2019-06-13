# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class UpdateNetworkDeviceWirelessRadioSettingsModel(object):

    """Implementation of the 'updateNetworkDeviceWirelessRadioSettings' model.

    TODO: type model description here.

    Attributes:
        rf_profile_id (int): The ID of an RF profile to assign to the device.
            If the value of this parameter is null, the appropriate basic RF
            profile (indoor or outdoor) will be assigned to the device.
            Assigning an RF profile will clear ALL manually configured
            overrides on the device (channel width, channel, power).

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "rf_profile_id":'rfProfileId'
    }

    def __init__(self,
                 rf_profile_id=None):
        """Constructor for the UpdateNetworkDeviceWirelessRadioSettingsModel class"""

        # Initialize members of the class
        self.rf_profile_id = rf_profile_id


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
        rf_profile_id = dictionary.get('rfProfileId')

        # Return an object of this model
        return cls(rf_profile_id)



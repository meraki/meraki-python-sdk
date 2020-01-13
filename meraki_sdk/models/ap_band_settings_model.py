# -*- coding: utf-8 -*-

"""
    meraki_sdk

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class ApBandSettingsModel(object):

    """Implementation of the 'ApBandSettings' model.

    Settings that will be enabled if selectionType is set to 'ap'.

    Attributes:
        band_operation_mode (BandOperationModeEnum): Choice between 'dual',
            '2.4ghz' or '5ghz'. Defaults to dual.
        band_steering_enabled (bool): Steers client to most open band. Can be
            either true or false. Defaults to true.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "band_operation_mode":'bandOperationMode',
        "band_steering_enabled":'bandSteeringEnabled'
    }

    def __init__(self,
                 band_operation_mode=None,
                 band_steering_enabled=None):
        """Constructor for the ApBandSettingsModel class"""

        # Initialize members of the class
        self.band_operation_mode = band_operation_mode
        self.band_steering_enabled = band_steering_enabled


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
        band_operation_mode = dictionary.get('bandOperationMode')
        band_steering_enabled = dictionary.get('bandSteeringEnabled')

        # Return an object of this model
        return cls(band_operation_mode,
                   band_steering_enabled)



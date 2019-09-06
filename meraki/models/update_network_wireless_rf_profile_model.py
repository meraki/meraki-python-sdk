# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""

import meraki.models.ap_band_settings1_model
import meraki.models.two_four_ghz_settings1_model
import meraki.models.five_ghz_settings1_model

class UpdateNetworkWirelessRfProfileModel(object):

    """Implementation of the 'updateNetworkWirelessRfProfile' model.

    TODO: type model description here.

    Attributes:
        name (string): The name of the new profile. Must be unique.
        client_balancing_enabled (bool): Steers client to best available
            access point. Can be either true or false.
        min_bitrate_type (MinBitrateType1Enum): Minimum bitrate can be set to
            either 'band' or 'ssid'.
        band_selection_type (BandSelectionType1Enum): Band selection can be
            set to either 'ssid' or 'ap'.
        ap_band_settings (ApBandSettings1Model): Settings that will be enabled
            if selectionType is set to 'ap'.
        two_four_ghz_settings (TwoFourGhzSettings1Model): Settings related to
            2.4Ghz band
        five_ghz_settings (FiveGhzSettings1Model): Settings related to 5Ghz
            band

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name":'name',
        "client_balancing_enabled":'clientBalancingEnabled',
        "min_bitrate_type":'minBitrateType',
        "band_selection_type":'bandSelectionType',
        "ap_band_settings":'apBandSettings',
        "two_four_ghz_settings":'twoFourGhzSettings',
        "five_ghz_settings":'fiveGhzSettings'
    }

    def __init__(self,
                 name=None,
                 client_balancing_enabled=None,
                 min_bitrate_type=None,
                 band_selection_type=None,
                 ap_band_settings=None,
                 two_four_ghz_settings=None,
                 five_ghz_settings=None):
        """Constructor for the UpdateNetworkWirelessRfProfileModel class"""

        # Initialize members of the class
        self.name = name
        self.client_balancing_enabled = client_balancing_enabled
        self.min_bitrate_type = min_bitrate_type
        self.band_selection_type = band_selection_type
        self.ap_band_settings = ap_band_settings
        self.two_four_ghz_settings = two_four_ghz_settings
        self.five_ghz_settings = five_ghz_settings


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
        client_balancing_enabled = dictionary.get('clientBalancingEnabled')
        min_bitrate_type = dictionary.get('minBitrateType')
        band_selection_type = dictionary.get('bandSelectionType')
        ap_band_settings = meraki.models.ap_band_settings1_model.ApBandSettings1Model.from_dictionary(dictionary.get('apBandSettings')) if dictionary.get('apBandSettings') else None
        two_four_ghz_settings = meraki.models.two_four_ghz_settings1_model.TwoFourGhzSettings1Model.from_dictionary(dictionary.get('twoFourGhzSettings')) if dictionary.get('twoFourGhzSettings') else None
        five_ghz_settings = meraki.models.five_ghz_settings1_model.FiveGhzSettings1Model.from_dictionary(dictionary.get('fiveGhzSettings')) if dictionary.get('fiveGhzSettings') else None

        # Return an object of this model
        return cls(name,
                   client_balancing_enabled,
                   min_bitrate_type,
                   band_selection_type,
                   ap_band_settings,
                   two_four_ghz_settings,
                   five_ghz_settings)



# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class TwoFourGhzSettingsModel(object):

    """Implementation of the 'TwoFourGhzSettings' model.

    Settings related to 2.4Ghz band

    Attributes:
        max_power (int): Sets max power (dBm) of 2.4Ghz band. Can be integer
            between 5 and 30. Defaults to 30.
        min_power (int): Sets min power (dBm) of 2.4Ghz band. Can be integer
            between 5 and 30. Defaults to 5.
        min_bitrate (float): Sets min bitrate (Mbps) of 2.4Ghz band. Can be
            one of '1', '2', '5.5', '6', '9', '11', '12', '18', '24', '36',
            '48' or '54'. Defaults to 11.
        valid_auto_channels (list of int): Sets valid auto channels for 2.4Ghz
            band. Can be one of '1', '6' or '11'. Defaults to [1, 6, 11].
        ax_enabled (bool): Determines whether ax radio on 2.4Ghz band is on or
            off. Can be either true or false. If false, we highly recommend
            disabling band steering. Defaults to true.
        rxsop (int): The RX-SOP level controls the sensitivity of the radio.
            It is strongly recommended to use RX-SOP only after     consulting
            a wireless expert. RX-SOP can be configured in the range of -65 to
            -95 (dBm). A value of null will     reset this to the default.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "max_power":'maxPower',
        "min_power":'minPower',
        "min_bitrate":'minBitrate',
        "valid_auto_channels":'validAutoChannels',
        "ax_enabled":'axEnabled',
        "rxsop":'rxsop'
    }

    def __init__(self,
                 max_power=None,
                 min_power=None,
                 min_bitrate=None,
                 valid_auto_channels=None,
                 ax_enabled=None,
                 rxsop=None):
        """Constructor for the TwoFourGhzSettingsModel class"""

        # Initialize members of the class
        self.max_power = max_power
        self.min_power = min_power
        self.min_bitrate = min_bitrate
        self.valid_auto_channels = valid_auto_channels
        self.ax_enabled = ax_enabled
        self.rxsop = rxsop


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
        max_power = dictionary.get('maxPower')
        min_power = dictionary.get('minPower')
        min_bitrate = dictionary.get('minBitrate')
        valid_auto_channels = dictionary.get('validAutoChannels')
        ax_enabled = dictionary.get('axEnabled')
        rxsop = dictionary.get('rxsop')

        # Return an object of this model
        return cls(max_power,
                   min_power,
                   min_bitrate,
                   valid_auto_channels,
                   ax_enabled,
                   rxsop)



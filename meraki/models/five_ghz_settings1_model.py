# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class FiveGhzSettings1Model(object):

    """Implementation of the 'FiveGhzSettings1' model.

    Settings related to 5Ghz band

    Attributes:
        max_power (int): Sets max power (dBm) of 5Ghz band. Can be integer
            between 8 and 30.
        min_power (int): Sets min power (dBm) of 5Ghz band. Can be integer
            between 8 and 30.
        min_bitrate (string): Sets min bitrate (Mbps) of 5Ghz band. Can be one
            of '6', '9', '12', '18', '24', '36', '48' or '54'.
        valid_auto_channels (list of int): Sets valid auto channels for 5Ghz
            band. Can be one of '36', '40', '44', '48', '52', '56', '60',
            '64', '100', '104', '108', '112', '116', '120', '124', '128',
            '132', '136', '140', '144', '149', '153', '157', '161' or '165'.
        channel_width (string): Sets channel width (MHz) for 5Ghz band. Can be
            one of 'auto', '20', '40' or '80'.
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
        "channel_width":'channelWidth',
        "rxsop":'rxsop'
    }

    def __init__(self,
                 max_power=None,
                 min_power=None,
                 min_bitrate=None,
                 valid_auto_channels=None,
                 channel_width=None,
                 rxsop=None):
        """Constructor for the FiveGhzSettings1Model class"""

        # Initialize members of the class
        self.max_power = max_power
        self.min_power = min_power
        self.min_bitrate = min_bitrate
        self.valid_auto_channels = valid_auto_channels
        self.channel_width = channel_width
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
        channel_width = dictionary.get('channelWidth')
        rxsop = dictionary.get('rxsop')

        # Return an object of this model
        return cls(max_power,
                   min_power,
                   min_bitrate,
                   valid_auto_channels,
                   channel_width,
                   rxsop)



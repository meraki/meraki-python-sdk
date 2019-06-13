# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class BlinkNetworkDeviceLedsModel(object):

    """Implementation of the 'blinkNetworkDeviceLeds' model.

    TODO: type model description here.

    Attributes:
        duration (int): The duration in seconds. Must be between 5 and 120.
            Default is 20 seconds
        period (int): The period in milliseconds. Must be between 100 and
            1000. Default is 160 milliseconds
        duty (int): The duty cycle as the percent active. Must be between 10
            and 90. Default is 50.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "duration":'duration',
        "period":'period',
        "duty":'duty'
    }

    def __init__(self,
                 duration=None,
                 period=None,
                 duty=None):
        """Constructor for the BlinkNetworkDeviceLedsModel class"""

        # Initialize members of the class
        self.duration = duration
        self.period = period
        self.duty = duty


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
        duration = dictionary.get('duration')
        period = dictionary.get('period')
        duty = dictionary.get('duty')

        # Return an object of this model
        return cls(duration,
                   period,
                   duty)



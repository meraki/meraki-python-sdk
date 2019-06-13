# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class BandwidthLimits1Model(object):

    """Implementation of the 'BandwidthLimits1' model.

    The bandwidth limits object, specifying the upload ('limitUp') and
    download ('limitDown') speed in Kbps. These are only enforced if
    'settings' is set to 'custom'.

    Attributes:
        limit_up (int): The maximum upload limit (integer, in Kbps).
        limit_down (int): The maximum download limit (integer, in Kbps).

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "limit_up":'limitUp',
        "limit_down":'limitDown'
    }

    def __init__(self,
                 limit_up=None,
                 limit_down=None):
        """Constructor for the BandwidthLimits1Model class"""

        # Initialize members of the class
        self.limit_up = limit_up
        self.limit_down = limit_down


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
        limit_up = dictionary.get('limitUp')
        limit_down = dictionary.get('limitDown')

        # Return an object of this model
        return cls(limit_up,
                   limit_down)



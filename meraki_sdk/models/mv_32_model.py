# -*- coding: utf-8 -*-

"""
    meraki_sdk

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class MV32Model(object):

    """Implementation of the 'MV32' model.

    Quality and resolution for MV32 camera models.

    Attributes:
        quality (Quality3Enum): Quality of the camera. Can be one of
            'Standard' or 'Enhanced'.
        resolution (Resolution2Enum): Resolution of the camera. Can be one of
            '1080x1080' or '2058x2058'.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "quality":'quality',
        "resolution":'resolution'
    }

    def __init__(self,
                 quality=None,
                 resolution=None):
        """Constructor for the MV32Model class"""

        # Initialize members of the class
        self.quality = quality
        self.resolution = resolution


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
        quality = dictionary.get('quality')
        resolution = dictionary.get('resolution')

        # Return an object of this model
        return cls(quality,
                   resolution)



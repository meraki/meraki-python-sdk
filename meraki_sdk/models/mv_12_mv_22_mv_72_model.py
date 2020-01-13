# -*- coding: utf-8 -*-

"""
    meraki_sdk

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class MV12MV22MV72Model(object):

    """Implementation of the 'MV12MV22MV72' model.

    Quality and resolution for MV12/MV22/MV72 camera models.

    Attributes:
        quality (Quality1Enum): Quality of the camera. Can be one of
            'Standard', 'Enhanced' or 'High'.
        resolution (Resolution1Enum): Resolution of the camera. Can be one of
            '1280x720' or '1920x1080'.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "quality":'quality',
        "resolution":'resolution'
    }

    def __init__(self,
                 quality=None,
                 resolution=None):
        """Constructor for the MV12MV22MV72Model class"""

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



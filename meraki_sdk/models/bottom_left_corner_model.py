# -*- coding: utf-8 -*-

"""
    meraki_sdk

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class BottomLeftCornerModel(object):

    """Implementation of the 'BottomLeftCorner' model.

    The longitude and latitude of the bottom left corner of your floor plan.

    Attributes:
        lat (float): Latitude
        lng (float): Longitude

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "lat":'lat',
        "lng":'lng'
    }

    def __init__(self,
                 lat=None,
                 lng=None):
        """Constructor for the BottomLeftCornerModel class"""

        # Initialize members of the class
        self.lat = lat
        self.lng = lng


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
        lat = dictionary.get('lat')
        lng = dictionary.get('lng')

        # Return an object of this model
        return cls(lat,
                   lng)



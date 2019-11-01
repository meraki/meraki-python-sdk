# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class Center1Model(object):

    """Implementation of the 'Center1' model.

    The longitude and latitude of the center of your floor plan. If you want
    to change the geolocation data of your floor plan, either the 'center' or
    two adjacent corners (e.g. 'topLeftCorner' and 'bottomLeftCorner') must be
    specified. If 'center' is specified, the floor plan is placed over that
    point with no rotation. If two adjacent corners are specified, the floor
    plan is rotated to line up with the two specified points. The aspect ratio
    of the floor plan's image is preserved regardless of which corners/center
    are specified. (This means if that more than two corners are specified,
    only two corners may be used to preserve the floor plan's aspect ratio.).
    No two points can have the same latitude, longitude pair.

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
        """Constructor for the Center1Model class"""

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



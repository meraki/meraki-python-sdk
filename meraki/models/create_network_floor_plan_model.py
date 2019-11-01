# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""

import meraki.models.center_model
import meraki.models.bottom_left_corner_model
import meraki.models.bottom_right_corner_model
import meraki.models.top_left_corner_model
import meraki.models.top_right_corner_model

class CreateNetworkFloorPlanModel(object):

    """Implementation of the 'createNetworkFloorPlan' model.

    TODO: type model description here.

    Attributes:
        name (string): The name of your floor plan.
        center (CenterModel): The longitude and latitude of the center of your
            floor plan. The 'center' or two adjacent corners (e.g.
            'topLeftCorner' and 'bottomLeftCorner') must be specified. If
            'center' is specified, the floor plan is placed over that point
            with no rotation. If two adjacent corners are specified, the floor
            plan is rotated to line up with the two specified points. The
            aspect ratio of the floor plan's image is preserved regardless of
            which corners/center are specified. (This means if that more than
            two corners are specified, only two corners may be used to
            preserve the floor plan's aspect ratio.). No two points can have
            the same latitude, longitude pair.
        bottom_left_corner (BottomLeftCornerModel): The longitude and latitude
            of the bottom left corner of your floor plan.
        bottom_right_corner (BottomRightCornerModel): The longitude and
            latitude of the bottom right corner of your floor plan.
        top_left_corner (TopLeftCornerModel): The longitude and latitude of
            the top left corner of your floor plan.
        top_right_corner (TopRightCornerModel): The longitude and latitude of
            the top right corner of your floor plan.
        image_contents (string): The file contents (a base 64 encoded string)
            of your image. Supported formats are PNG, GIF, and JPG. Note that
            all images are saved as PNG files, regardless of the format they
            are uploaded in.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name":'name',
        "image_contents":'imageContents',
        "center":'center',
        "bottom_left_corner":'bottomLeftCorner',
        "bottom_right_corner":'bottomRightCorner',
        "top_left_corner":'topLeftCorner',
        "top_right_corner":'topRightCorner'
    }

    def __init__(self,
                 name=None,
                 image_contents=None,
                 center=None,
                 bottom_left_corner=None,
                 bottom_right_corner=None,
                 top_left_corner=None,
                 top_right_corner=None):
        """Constructor for the CreateNetworkFloorPlanModel class"""

        # Initialize members of the class
        self.name = name
        self.center = center
        self.bottom_left_corner = bottom_left_corner
        self.bottom_right_corner = bottom_right_corner
        self.top_left_corner = top_left_corner
        self.top_right_corner = top_right_corner
        self.image_contents = image_contents


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
        image_contents = dictionary.get('imageContents')
        center = meraki.models.center_model.CenterModel.from_dictionary(dictionary.get('center')) if dictionary.get('center') else None
        bottom_left_corner = meraki.models.bottom_left_corner_model.BottomLeftCornerModel.from_dictionary(dictionary.get('bottomLeftCorner')) if dictionary.get('bottomLeftCorner') else None
        bottom_right_corner = meraki.models.bottom_right_corner_model.BottomRightCornerModel.from_dictionary(dictionary.get('bottomRightCorner')) if dictionary.get('bottomRightCorner') else None
        top_left_corner = meraki.models.top_left_corner_model.TopLeftCornerModel.from_dictionary(dictionary.get('topLeftCorner')) if dictionary.get('topLeftCorner') else None
        top_right_corner = meraki.models.top_right_corner_model.TopRightCornerModel.from_dictionary(dictionary.get('topRightCorner')) if dictionary.get('topRightCorner') else None

        # Return an object of this model
        return cls(name,
                   image_contents,
                   center,
                   bottom_left_corner,
                   bottom_right_corner,
                   top_left_corner,
                   top_right_corner)



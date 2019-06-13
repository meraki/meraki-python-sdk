# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class GenerateNetworkCameraSnapshotModel(object):

    """Implementation of the 'generateNetworkCameraSnapshot' model.

    TODO: type model description here.

    Attributes:
        timestamp (string): [optional] The snapshot will be taken from this
            time on the camera. The timestamp is expected to be in ISO 8601
            format. If no timestamp is specified, we will assume current
            time.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "timestamp":'timestamp'
    }

    def __init__(self,
                 timestamp=None):
        """Constructor for the GenerateNetworkCameraSnapshotModel class"""

        # Initialize members of the class
        self.timestamp = timestamp


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
        timestamp = dictionary.get('timestamp')

        # Return an object of this model
        return cls(timestamp)



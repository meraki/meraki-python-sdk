# -*- coding: utf-8 -*-

"""
    meraki_sdk

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class ReservedIpRangeModel(object):

    """Implementation of the 'ReservedIpRange' model.

    TODO: type model description here.

    Attributes:
        start (string): Starting IP included in the reserved range of IPs
        end (string): Ending IP included in the reserved range of IPs
        comment (string): Comment explaining the reserved IP range

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "start":'start',
        "end":'end',
        "comment":'comment'
    }

    def __init__(self,
                 start=None,
                 end=None,
                 comment=None):
        """Constructor for the ReservedIpRangeModel class"""

        # Initialize members of the class
        self.start = start
        self.end = end
        self.comment = comment


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
        start = dictionary.get('start')
        end = dictionary.get('end')
        comment = dictionary.get('comment')

        # Return an object of this model
        return cls(start,
                   end,
                   comment)



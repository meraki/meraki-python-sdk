# -*- coding: utf-8 -*-

"""
    meraki_sdk

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class MappingModel(object):

    """Implementation of the 'Mapping' model.

    TODO: type model description here.

    Attributes:
        dscp (int): The Differentiated Services Code Point (DSCP) tag in the
            IP header that will be mapped to a particular Class-of-Service
            (CoS) queue. Value can be in the range of 0 to 63 inclusive.
        cos (int): The actual layer-2 CoS queue the DSCP value is mapped to.
            These are not bits set on outgoing frames. Value can be in the
            range of 0 to 5 inclusive.
        title (string): Label for the mapping (optional).

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "dscp":'dscp',
        "cos":'cos',
        "title":'title'
    }

    def __init__(self,
                 dscp=None,
                 cos=None,
                 title=None):
        """Constructor for the MappingModel class"""

        # Initialize members of the class
        self.dscp = dscp
        self.cos = cos
        self.title = title


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
        dscp = dictionary.get('dscp')
        cos = dictionary.get('cos')
        title = dictionary.get('title')

        # Return an object of this model
        return cls(dscp,
                   cos,
                   title)



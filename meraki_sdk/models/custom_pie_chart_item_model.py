# -*- coding: utf-8 -*-

"""
    meraki_sdk

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class CustomPieChartItemModel(object):

    """Implementation of the 'CustomPieChartItem' model.

    TODO: type model description here.

    Attributes:
        name (string): The name of the custom pie chart item.
        mtype (Type7Enum): The signature type for the custom pie chart item.
            Can be one of 'host', 'port' or 'ipRange'.
        value (string): The value of the custom pie chart item. Valid syntax
            depends on the signature type of the chart item     (see sample
            request/response for more details).

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name":'name',
        "mtype":'type',
        "value":'value'
    }

    def __init__(self,
                 name=None,
                 mtype=None,
                 value=None):
        """Constructor for the CustomPieChartItemModel class"""

        # Initialize members of the class
        self.name = name
        self.mtype = mtype
        self.value = value


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
        mtype = dictionary.get('type')
        value = dictionary.get('value')

        # Return an object of this model
        return cls(name,
                   mtype,
                   value)



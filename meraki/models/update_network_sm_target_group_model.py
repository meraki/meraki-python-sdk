# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class UpdateNetworkSmTargetGroupModel(object):

    """Implementation of the 'updateNetworkSmTargetGroup' model.

    TODO: type model description here.

    Attributes:
        name (string): The name of this target group
        scope (string): The scope and tag options of the target group. Comma
            separated values beginning with one of withAny, withAll,
            withoutAny, withoutAll, all, none, followed by tags. Default to
            none if empty.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name":'name',
        "scope":'scope'
    }

    def __init__(self,
                 name=None,
                 scope=None):
        """Constructor for the UpdateNetworkSmTargetGroupModel class"""

        # Initialize members of the class
        self.name = name
        self.scope = scope


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
        scope = dictionary.get('scope')

        # Return an object of this model
        return cls(name,
                   scope)



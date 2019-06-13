# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class ActionModel(object):

    """Implementation of the 'Action' model.

    TODO: type model description here.

    Attributes:
        resource (string): Unique identifier for the resource to be acted on
        operation (string): The operation to be used. One of "create",
            "update", "destroy".
        body (string): The body of the action

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "resource":'resource',
        "operation":'operation',
        "body":'body'
    }

    def __init__(self,
                 resource=None,
                 operation=None,
                 body=None):
        """Constructor for the ActionModel class"""

        # Initialize members of the class
        self.resource = resource
        self.operation = operation
        self.body = body


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
        resource = dictionary.get('resource')
        operation = dictionary.get('operation')
        body = dictionary.get('body')

        # Return an object of this model
        return cls(resource,
                   operation,
                   body)



# -*- coding: utf-8 -*-

"""
    meraki_sdk

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class CreateNetworkSmBypassActivationLockAttemptModel(object):

    """Implementation of the 'createNetworkSmBypassActivationLockAttempt' model.

    TODO: type model description here.

    Attributes:
        ids (list of string): The ids of the devices to attempt activation
            lock bypass.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "ids":'ids'
    }

    def __init__(self,
                 ids=None):
        """Constructor for the CreateNetworkSmBypassActivationLockAttemptModel class"""

        # Initialize members of the class
        self.ids = ids


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
        ids = dictionary.get('ids')

        # Return an object of this model
        return cls(ids)



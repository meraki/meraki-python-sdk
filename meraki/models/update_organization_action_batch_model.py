# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class UpdateOrganizationActionBatchModel(object):

    """Implementation of the 'updateOrganizationActionBatch' model.

    TODO: type model description here.

    Attributes:
        confirmed (string): A boolean representing whether or not the batch
            has been confirmed. This property cannot be unset once it is
            true.
        synchronous (string): Force the batch to run synchronous. There can be
            at most 20 actions in synchronous batch.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "confirmed":'confirmed',
        "synchronous":'synchronous'
    }

    def __init__(self,
                 confirmed=None,
                 synchronous=None):
        """Constructor for the UpdateOrganizationActionBatchModel class"""

        # Initialize members of the class
        self.confirmed = confirmed
        self.synchronous = synchronous


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
        confirmed = dictionary.get('confirmed')
        synchronous = dictionary.get('synchronous')

        # Return an object of this model
        return cls(confirmed,
                   synchronous)



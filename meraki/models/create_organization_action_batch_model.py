# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""

import meraki.models.action_model

class CreateOrganizationActionBatchModel(object):

    """Implementation of the 'createOrganizationActionBatch' model.

    TODO: type model description here.

    Attributes:
        confirmed (string): Set to true for immediate execution. Set to false
            if the action should be previewed before executing.
        synchronous (string): Force the batch to run synchronous. There can be
            at most 20 actions in synchronous batch.
        actions (list of ActionModel): A set of changes to make as part of
            this action (<a
            href='https://developer.cisco.com/meraki/api/#/rest/guides/action-b
            atches/'>more details</a>)

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "confirmed":'confirmed',
        "synchronous":'synchronous',
        "actions":'actions'
    }

    def __init__(self,
                 confirmed=None,
                 synchronous=None,
                 actions=None):
        """Constructor for the CreateOrganizationActionBatchModel class"""

        # Initialize members of the class
        self.confirmed = confirmed
        self.synchronous = synchronous
        self.actions = actions


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
        actions = None
        if dictionary.get('actions') != None:
            actions = list()
            for structure in dictionary.get('actions'):
                actions.append(meraki.models.action_model.ActionModel.from_dictionary(structure))

        # Return an object of this model
        return cls(confirmed,
                   synchronous,
                   actions)



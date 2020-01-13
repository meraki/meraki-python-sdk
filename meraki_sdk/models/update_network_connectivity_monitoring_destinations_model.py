# -*- coding: utf-8 -*-

"""
    meraki_sdk

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""

import meraki_sdk.models.destination_model

class UpdateNetworkConnectivityMonitoringDestinationsModel(object):

    """Implementation of the 'updateNetworkConnectivityMonitoringDestinations' model.

    TODO: type model description here.

    Attributes:
        destinations (list of DestinationModel): The list of connectivity
            monitoring destinations

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "destinations":'destinations'
    }

    def __init__(self,
                 destinations=None):
        """Constructor for the UpdateNetworkConnectivityMonitoringDestinationsModel class"""

        # Initialize members of the class
        self.destinations = destinations


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
        destinations = None
        if dictionary.get('destinations') != None:
            destinations = list()
            for structure in dictionary.get('destinations'):
                destinations.append(meraki_sdk.models.destination_model.DestinationModel.from_dictionary(structure))

        # Return an object of this model
        return cls(destinations)



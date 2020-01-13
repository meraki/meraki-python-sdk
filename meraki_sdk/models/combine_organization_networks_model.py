# -*- coding: utf-8 -*-

"""
    meraki_sdk

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class CombineOrganizationNetworksModel(object):

    """Implementation of the 'combineOrganizationNetworks' model.

    TODO: type model description here.

    Attributes:
        name (string): The name of the combined network
        network_ids (list of string): A list of the network IDs that will be
            combined. If an ID of a combined network is included in this list,
            the other networks in the list will be grouped into that network
        enrollment_string (string): A unique identifier which can be used for
            device enrollment or easy access through the Meraki SM
            Registration page or the Self Service Portal. Please note that
            changing this field may cause existing bookmarks to break. All
            networks that are part of this combined network will have their
            enrollment string appended by '-network_type'. If left empty, all
            exisitng enrollment strings will be deleted.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name":'name',
        "network_ids":'networkIds',
        "enrollment_string":'enrollmentString'
    }

    def __init__(self,
                 name=None,
                 network_ids=None,
                 enrollment_string=None):
        """Constructor for the CombineOrganizationNetworksModel class"""

        # Initialize members of the class
        self.name = name
        self.network_ids = network_ids
        self.enrollment_string = enrollment_string


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
        network_ids = dictionary.get('networkIds')
        enrollment_string = dictionary.get('enrollmentString')

        # Return an object of this model
        return cls(name,
                   network_ids,
                   enrollment_string)



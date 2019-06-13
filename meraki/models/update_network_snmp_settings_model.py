# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""

import meraki.models.user_model

class UpdateNetworkSnmpSettingsModel(object):

    """Implementation of the 'updateNetworkSnmpSettings' model.

    TODO: type model description here.

    Attributes:
        access (AccessEnum): The type of SNMP access. Can be one of 'none'
            (disabled), 'community' (V1/V2c), or 'users' (V3).
        community_string (string): The SNMP community string. Only relevant if
            'access' is set to 'community'.
        users (list of UserModel): The list of SNMP users. Only relevant if
            'access' is set to 'users'.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "access":'access',
        "community_string":'communityString',
        "users":'users'
    }

    def __init__(self,
                 access=None,
                 community_string=None,
                 users=None):
        """Constructor for the UpdateNetworkSnmpSettingsModel class"""

        # Initialize members of the class
        self.access = access
        self.community_string = community_string
        self.users = users


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
        access = dictionary.get('access')
        community_string = dictionary.get('communityString')
        users = None
        if dictionary.get('users') != None:
            users = list()
            for structure in dictionary.get('users'):
                users.append(meraki.models.user_model.UserModel.from_dictionary(structure))

        # Return an object of this model
        return cls(access,
                   community_string,
                   users)



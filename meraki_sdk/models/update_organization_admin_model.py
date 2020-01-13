# -*- coding: utf-8 -*-

"""
    meraki_sdk

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""

import meraki_sdk.models.tag_model
import meraki_sdk.models.network_model

class UpdateOrganizationAdminModel(object):

    """Implementation of the 'updateOrganizationAdmin' model.

    TODO: type model description here.

    Attributes:
        name (string): The name of the dashboard administrator
        org_access (OrgAccessEnum): The privilege of the dashboard
            administrator on the organization. Can be one of 'full',
            'read-only', 'enterprise' or 'none'
        tags (list of TagModel): The list of tags that the dashboard
            administrator has privileges on
        networks (list of NetworkModel): The list of networks that the
            dashboard administrator has privileges on

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name":'name',
        "org_access":'orgAccess',
        "tags":'tags',
        "networks":'networks'
    }

    def __init__(self,
                 name=None,
                 org_access=None,
                 tags=None,
                 networks=None):
        """Constructor for the UpdateOrganizationAdminModel class"""

        # Initialize members of the class
        self.name = name
        self.org_access = org_access
        self.tags = tags
        self.networks = networks


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
        org_access = dictionary.get('orgAccess')
        tags = None
        if dictionary.get('tags') != None:
            tags = list()
            for structure in dictionary.get('tags'):
                tags.append(meraki_sdk.models.tag_model.TagModel.from_dictionary(structure))
        networks = None
        if dictionary.get('networks') != None:
            networks = list()
            for structure in dictionary.get('networks'):
                networks.append(meraki_sdk.models.network_model.NetworkModel.from_dictionary(structure))

        # Return an object of this model
        return cls(name,
                   org_access,
                   tags,
                   networks)



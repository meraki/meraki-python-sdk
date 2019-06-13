# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class Rule5Model(object):

    """Implementation of the 'Rule5' model.

    TODO: type model description here.

    Attributes:
        description (string): A description for your Bonjour forwarding rule.
            Optional.
        vlan_id (string): The ID of the service VLAN. Required.
        services (list of ServiceEnum): A list of Bonjour services. At least
            one service must be specified. Available services are 'All
            Services', 'AirPlay', 'AFP', 'BitTorrent', 'FTP', 'iChat',
            'iTunes', 'Printers', 'Samba', 'Scanners' and 'SSH'

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "vlan_id":'vlanId',
        "services":'services',
        "description":'description'
    }

    def __init__(self,
                 vlan_id=None,
                 services=None,
                 description=None):
        """Constructor for the Rule5Model class"""

        # Initialize members of the class
        self.description = description
        self.vlan_id = vlan_id
        self.services = services


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
        vlan_id = dictionary.get('vlanId')
        services = dictionary.get('services')
        description = dictionary.get('description')

        # Return an object of this model
        return cls(vlan_id,
                   services,
                   description)



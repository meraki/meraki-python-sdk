# -*- coding: utf-8 -*-

"""
    meraki_sdk

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class FixedIpAssignmentModel(object):

    """Implementation of the 'FixedIpAssignment' model.

    TODO: type model description here.

    Attributes:
        name (string): A descriptive name of the assignment
        ip (string): The IP address you want to assign to a specific server or
            device
        mac (string): The MAC address of the server or device that hosts the
            internal resource that you wish to receive the specified IP
            address

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "ip":'ip',
        "mac":'mac',
        "name":'name'
    }

    def __init__(self,
                 ip=None,
                 mac=None,
                 name=None):
        """Constructor for the FixedIpAssignmentModel class"""

        # Initialize members of the class
        self.name = name
        self.ip = ip
        self.mac = mac


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
        ip = dictionary.get('ip')
        mac = dictionary.get('mac')
        name = dictionary.get('name')

        # Return an object of this model
        return cls(ip,
                   mac,
                   name)



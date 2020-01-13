# -*- coding: utf-8 -*-

"""
    meraki_sdk

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class SwitchProfilePortModel(object):

    """Implementation of the 'SwitchProfilePort' model.

    TODO: type model description here.

    Attributes:
        profile (string): Profile identifier.
        port_id (string): Port identifier of switch port. For modules, the
            identifier is "SlotNumber_ModuleType_PortNumber" (Ex:
            “1_8X10G_1”), otherwise it is just the port number (Ex: "8").

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "profile":'profile',
        "port_id":'portId'
    }

    def __init__(self,
                 profile=None,
                 port_id=None):
        """Constructor for the SwitchProfilePortModel class"""

        # Initialize members of the class
        self.profile = profile
        self.port_id = port_id


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
        profile = dictionary.get('profile')
        port_id = dictionary.get('portId')

        # Return an object of this model
        return cls(profile,
                   port_id)



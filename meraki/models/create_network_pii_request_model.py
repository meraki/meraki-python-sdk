# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class CreateNetworkPiiRequestModel(object):

    """Implementation of the 'createNetworkPiiRequest' model.

    TODO: type model description here.

    Attributes:
        mtype (Type5Enum): One of "delete" or "restrict processing"
        datasets (list of string): The datasets related to the provided key
            that should be deleted. Only applies to "delete" requests. The
            value "all" will be expanded to all datasets applicable to this
            type. The datasets by applicable to each type are: mac (usage,
            events, traffic), email (users, loginAttempts), username (users,
            loginAttempts), bluetoothMac (client, connectivity), smDeviceId
            (device), smUserId (user)
        username (string): The username of a network log in. Only applies to
            "delete" requests.
        email (string): The email of a network user account. Only applies to
            "delete" requests.
        mac (string): The MAC of a network client device. Applies to both
            "restrict processing" and "delete" requests.
        sm_device_id (string): The sm_device_id of a Systems Manager device.
            The only way to "restrict processing" or "delete" a Systems
            Manager device. Must include "device" in the dataset for a
            "delete" request to destroy the device.
        sm_user_id (string): The sm_user_id of a Systems Manager user. The
            only way to "restrict processing" or "delete" a Systems Manager
            user. Must include "user" in the dataset for a "delete" request to
            destroy the user.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "mtype":'type',
        "datasets":'datasets',
        "username":'username',
        "email":'email',
        "mac":'mac',
        "sm_device_id":'smDeviceId',
        "sm_user_id":'smUserId'
    }

    def __init__(self,
                 mtype=None,
                 datasets=None,
                 username=None,
                 email=None,
                 mac=None,
                 sm_device_id=None,
                 sm_user_id=None):
        """Constructor for the CreateNetworkPiiRequestModel class"""

        # Initialize members of the class
        self.mtype = mtype
        self.datasets = datasets
        self.username = username
        self.email = email
        self.mac = mac
        self.sm_device_id = sm_device_id
        self.sm_user_id = sm_user_id


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
        mtype = dictionary.get('type')
        datasets = dictionary.get('datasets')
        username = dictionary.get('username')
        email = dictionary.get('email')
        mac = dictionary.get('mac')
        sm_device_id = dictionary.get('smDeviceId')
        sm_user_id = dictionary.get('smUserId')

        # Return an object of this model
        return cls(mtype,
                   datasets,
                   username,
                   email,
                   mac,
                   sm_device_id,
                   sm_user_id)



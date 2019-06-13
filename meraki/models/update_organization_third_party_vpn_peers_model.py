# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""

import meraki.models.peer_model

class UpdateOrganizationThirdPartyVPNPeersModel(object):

    """Implementation of the 'updateOrganizationThirdPartyVPNPeers' model.

    TODO: type model description here.

    Attributes:
        peers (list of PeerModel): The list of VPN peers

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "peers":'peers'
    }

    def __init__(self,
                 peers=None):
        """Constructor for the UpdateOrganizationThirdPartyVPNPeersModel class"""

        # Initialize members of the class
        self.peers = peers


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
        peers = None
        if dictionary.get('peers') != None:
            peers = list()
            for structure in dictionary.get('peers'):
                peers.append(meraki.models.peer_model.PeerModel.from_dictionary(structure))

        # Return an object of this model
        return cls(peers)



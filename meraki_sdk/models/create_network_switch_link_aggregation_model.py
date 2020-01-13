# -*- coding: utf-8 -*-

"""
    meraki_sdk

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""

import meraki_sdk.models.switch_port_model
import meraki_sdk.models.switch_profile_port_model

class CreateNetworkSwitchLinkAggregationModel(object):

    """Implementation of the 'createNetworkSwitchLinkAggregation' model.

    TODO: type model description here.

    Attributes:
        switch_ports (list of SwitchPortModel): Array of switch or stack ports
            for creating aggregation group. Minimum 2 and maximum 8 ports are
            supported.
        switch_profile_ports (list of SwitchProfilePortModel): Array of switch
            profile ports for creating aggregation group. Minimum 2 and
            maximum 8 ports are supported.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "switch_ports":'switchPorts',
        "switch_profile_ports":'switchProfilePorts'
    }

    def __init__(self,
                 switch_ports=None,
                 switch_profile_ports=None):
        """Constructor for the CreateNetworkSwitchLinkAggregationModel class"""

        # Initialize members of the class
        self.switch_ports = switch_ports
        self.switch_profile_ports = switch_profile_ports


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
        switch_ports = None
        if dictionary.get('switchPorts') != None:
            switch_ports = list()
            for structure in dictionary.get('switchPorts'):
                switch_ports.append(meraki_sdk.models.switch_port_model.SwitchPortModel.from_dictionary(structure))
        switch_profile_ports = None
        if dictionary.get('switchProfilePorts') != None:
            switch_profile_ports = list()
            for structure in dictionary.get('switchProfilePorts'):
                switch_profile_ports.append(meraki_sdk.models.switch_profile_port_model.SwitchProfilePortModel.from_dictionary(structure))

        # Return an object of this model
        return cls(switch_ports,
                   switch_profile_ports)



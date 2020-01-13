# -*- coding: utf-8 -*-

"""
    meraki_sdk

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""

import meraki_sdk.models.reserved_ip_range_model
import meraki_sdk.models.fixed_ip_assignment_model

class UpdateDeviceCellularGatewaySettingsModel(object):

    """Implementation of the 'updateDeviceCellularGatewaySettings' model.

    TODO: type model description here.

    Attributes:
        reserved_ip_ranges (list of ReservedIpRangeModel): list of all
            reserved IP ranges for a single MG
        fixed_ip_assignments (list of FixedIpAssignmentModel): list of all
            fixed IP assignments for a single MG

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "reserved_ip_ranges":'reservedIpRanges',
        "fixed_ip_assignments":'fixedIpAssignments'
    }

    def __init__(self,
                 reserved_ip_ranges=None,
                 fixed_ip_assignments=None):
        """Constructor for the UpdateDeviceCellularGatewaySettingsModel class"""

        # Initialize members of the class
        self.reserved_ip_ranges = reserved_ip_ranges
        self.fixed_ip_assignments = fixed_ip_assignments


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
        reserved_ip_ranges = None
        if dictionary.get('reservedIpRanges') != None:
            reserved_ip_ranges = list()
            for structure in dictionary.get('reservedIpRanges'):
                reserved_ip_ranges.append(meraki_sdk.models.reserved_ip_range_model.ReservedIpRangeModel.from_dictionary(structure))
        fixed_ip_assignments = None
        if dictionary.get('fixedIpAssignments') != None:
            fixed_ip_assignments = list()
            for structure in dictionary.get('fixedIpAssignments'):
                fixed_ip_assignments.append(meraki_sdk.models.fixed_ip_assignment_model.FixedIpAssignmentModel.from_dictionary(structure))

        # Return an object of this model
        return cls(reserved_ip_ranges,
                   fixed_ip_assignments)



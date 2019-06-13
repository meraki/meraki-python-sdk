# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""

import meraki.models.definition_model
import meraki.models.per_client_bandwidth_limits_model

class TrafficShapingRuleModel(object):

    """Implementation of the 'TrafficShapingRule' model.

    TODO: type model description here.

    Attributes:
        definitions (list of DefinitionModel): A list of objects describing
            the definitions of your traffic shaping rule. At least one
            definition is required.
        per_client_bandwidth_limits (PerClientBandwidthLimitsModel): An object
            describing the bandwidth settings for your rule.
        dscp_tag_value (int): The DSCP tag applied by your rule. null means
            'Do not change DSCP tag'.     For a list of possible tag values,
            use the trafficShaping/dscpTaggingOptions endpoint.
        pcp_tag_value (int): The PCP tag applied by your rule. Can be 0
            (lowest priority) through 7 (highest priority).     null means 'Do
            not set PCP tag'.
        priority (string): A string, indicating the priority level for packets
            bound to your rule.     Can be 'low', 'normal' or 'high'.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "definitions":'definitions',
        "per_client_bandwidth_limits":'perClientBandwidthLimits',
        "dscp_tag_value":'dscpTagValue',
        "pcp_tag_value":'pcpTagValue',
        "priority":'priority'
    }

    def __init__(self,
                 definitions=None,
                 per_client_bandwidth_limits=None,
                 dscp_tag_value=None,
                 pcp_tag_value=None,
                 priority=None):
        """Constructor for the TrafficShapingRuleModel class"""

        # Initialize members of the class
        self.definitions = definitions
        self.per_client_bandwidth_limits = per_client_bandwidth_limits
        self.dscp_tag_value = dscp_tag_value
        self.pcp_tag_value = pcp_tag_value
        self.priority = priority


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
        definitions = None
        if dictionary.get('definitions') != None:
            definitions = list()
            for structure in dictionary.get('definitions'):
                definitions.append(meraki.models.definition_model.DefinitionModel.from_dictionary(structure))
        per_client_bandwidth_limits = meraki.models.per_client_bandwidth_limits_model.PerClientBandwidthLimitsModel.from_dictionary(dictionary.get('perClientBandwidthLimits')) if dictionary.get('perClientBandwidthLimits') else None
        dscp_tag_value = dictionary.get('dscpTagValue')
        pcp_tag_value = dictionary.get('pcpTagValue')
        priority = dictionary.get('priority')

        # Return an object of this model
        return cls(definitions,
                   per_client_bandwidth_limits,
                   dscp_tag_value,
                   pcp_tag_value,
                   priority)



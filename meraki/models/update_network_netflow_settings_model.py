# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class UpdateNetworkNetflowSettingsModel(object):

    """Implementation of the 'updateNetworkNetflowSettings' model.

    TODO: type model description here.

    Attributes:
        reporting_enabled (bool): Boolean indicating whether NetFlow traffic
            reporting is enabled (true) or disabled (false).
        collector_ip (string): The IPv4 address of the NetFlow collector.
        collector_port (int): The port that the NetFlow collector will be
            listening on.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "reporting_enabled":'reportingEnabled',
        "collector_ip":'collectorIp',
        "collector_port":'collectorPort'
    }

    def __init__(self,
                 reporting_enabled=None,
                 collector_ip=None,
                 collector_port=None):
        """Constructor for the UpdateNetworkNetflowSettingsModel class"""

        # Initialize members of the class
        self.reporting_enabled = reporting_enabled
        self.collector_ip = collector_ip
        self.collector_port = collector_port


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
        reporting_enabled = dictionary.get('reportingEnabled')
        collector_ip = dictionary.get('collectorIp')
        collector_port = dictionary.get('collectorPort')

        # Return an object of this model
        return cls(reporting_enabled,
                   collector_ip,
                   collector_port)



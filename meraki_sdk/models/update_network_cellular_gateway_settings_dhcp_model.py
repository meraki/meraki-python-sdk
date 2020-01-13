# -*- coding: utf-8 -*-

"""
    meraki_sdk

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class UpdateNetworkCellularGatewaySettingsDhcpModel(object):

    """Implementation of the 'updateNetworkCellularGatewaySettingsDhcp' model.

    TODO: type model description here.

    Attributes:
        dhcp_lease_time (string): DHCP Lease time for all MG of the network.
            It can be '30 minutes', '1 hour', '4 hours', '12 hours', '1 day'
            or '1 week'.
        dns_nameservers (string): DNS name servers mode for all MG of the
            network. It can take 4 different values: 'upstream_dns',
            'google_dns', 'opendns', 'custom'.
        dns_custom_nameservers (list of string): list of fixed IP representing
            the the DNS Name servers when the mode is 'custom'

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "dhcp_lease_time":'dhcpLeaseTime',
        "dns_nameservers":'dnsNameservers',
        "dns_custom_nameservers":'dnsCustomNameservers'
    }

    def __init__(self,
                 dhcp_lease_time=None,
                 dns_nameservers=None,
                 dns_custom_nameservers=None):
        """Constructor for the UpdateNetworkCellularGatewaySettingsDhcpModel class"""

        # Initialize members of the class
        self.dhcp_lease_time = dhcp_lease_time
        self.dns_nameservers = dns_nameservers
        self.dns_custom_nameservers = dns_custom_nameservers


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
        dhcp_lease_time = dictionary.get('dhcpLeaseTime')
        dns_nameservers = dictionary.get('dnsNameservers')
        dns_custom_nameservers = dictionary.get('dnsCustomNameservers')

        # Return an object of this model
        return cls(dhcp_lease_time,
                   dns_nameservers,
                   dns_custom_nameservers)



# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""

import meraki.models.scheduling_model
import meraki.models.bandwidth_model
import meraki.models.firewall_and_traffic_shaping_model
import meraki.models.vlan_tagging_model
import meraki.models.bonjour_forwarding_model

class CreateNetworkGroupPolicyModel(object):

    """Implementation of the 'createNetworkGroupPolicy' model.

    TODO: type model description here.

    Attributes:
        name (string): The name for your group policy. Required.
        scheduling (SchedulingModel): The schedule for the group policy.
            Schedules are applied to days of the week.
        bandwidth (BandwidthModel): The bandwidth settings for clients bound
            to your group policy.
        firewall_and_traffic_shaping (FirewallAndTrafficShapingModel): The
            firewall and traffic shaping rules and settings for your policy.
        splash_auth_settings (SplashAuthSettingsEnum): Whether clients bound
            to your policy will bypass splash authorization or behave
            according to the network's rules. Can be one of 'network default'
            or 'bypass'. Only available if your network has a wireless
            configuration.
        vlan_tagging (VlanTaggingModel): The VLAN tagging settings for your
            group policy. Only available if your network has a wireless
            configuration.
        bonjour_forwarding (BonjourForwardingModel): The Bonjour settings for
            your group policy. Only valid if your network has a wireless
            configuration.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name":'name',
        "scheduling":'scheduling',
        "bandwidth":'bandwidth',
        "firewall_and_traffic_shaping":'firewallAndTrafficShaping',
        "splash_auth_settings":'splashAuthSettings',
        "vlan_tagging":'vlanTagging',
        "bonjour_forwarding":'bonjourForwarding'
    }

    def __init__(self,
                 name=None,
                 scheduling=None,
                 bandwidth=None,
                 firewall_and_traffic_shaping=None,
                 splash_auth_settings=None,
                 vlan_tagging=None,
                 bonjour_forwarding=None):
        """Constructor for the CreateNetworkGroupPolicyModel class"""

        # Initialize members of the class
        self.name = name
        self.scheduling = scheduling
        self.bandwidth = bandwidth
        self.firewall_and_traffic_shaping = firewall_and_traffic_shaping
        self.splash_auth_settings = splash_auth_settings
        self.vlan_tagging = vlan_tagging
        self.bonjour_forwarding = bonjour_forwarding


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
        name = dictionary.get('name')
        scheduling = meraki.models.scheduling_model.SchedulingModel.from_dictionary(dictionary.get('scheduling')) if dictionary.get('scheduling') else None
        bandwidth = meraki.models.bandwidth_model.BandwidthModel.from_dictionary(dictionary.get('bandwidth')) if dictionary.get('bandwidth') else None
        firewall_and_traffic_shaping = meraki.models.firewall_and_traffic_shaping_model.FirewallAndTrafficShapingModel.from_dictionary(dictionary.get('firewallAndTrafficShaping')) if dictionary.get('firewallAndTrafficShaping') else None
        splash_auth_settings = dictionary.get('splashAuthSettings')
        vlan_tagging = meraki.models.vlan_tagging_model.VlanTaggingModel.from_dictionary(dictionary.get('vlanTagging')) if dictionary.get('vlanTagging') else None
        bonjour_forwarding = meraki.models.bonjour_forwarding_model.BonjourForwardingModel.from_dictionary(dictionary.get('bonjourForwarding')) if dictionary.get('bonjourForwarding') else None

        # Return an object of this model
        return cls(name,
                   scheduling,
                   bandwidth,
                   firewall_and_traffic_shaping,
                   splash_auth_settings,
                   vlan_tagging,
                   bonjour_forwarding)



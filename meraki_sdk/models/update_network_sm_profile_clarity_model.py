# -*- coding: utf-8 -*-

"""
    meraki_sdk

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""

import meraki_sdk.models.vendor_config_model

class UpdateNetworkSmProfileClarityModel(object):

    """Implementation of the 'updateNetworkSmProfileClarity' model.

    TODO: type model description here.

    Attributes:
        name (string): optional: A new name for the profile
        scope (string): optional: A new scope for the profile (one of all,
            none, withAny, withAll, withoutAny, or withoutAll) and a set of
            tags of the devices to be assigned
        plugin_bundle_id (string): optional: The new bundle ID of the
            application
        filter_browsers (bool): optional: Whether or not to enable browser
            traffic filtering (one of true, false).
        filter_sockets (bool): optional: Whether or not to enable socket
            traffic filtering (one of true, false).
        vendor_config (list of VendorConfigModel): optional: The specific
            VendorConfig to be passed to the filtering framework, in the form
            of an array of objects (as JSON).

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name":'name',
        "scope":'scope',
        "plugin_bundle_id":'PluginBundleID',
        "filter_browsers":'FilterBrowsers',
        "filter_sockets":'FilterSockets',
        "vendor_config":'VendorConfig'
    }

    def __init__(self,
                 name=None,
                 scope=None,
                 plugin_bundle_id=None,
                 filter_browsers=None,
                 filter_sockets=None,
                 vendor_config=None):
        """Constructor for the UpdateNetworkSmProfileClarityModel class"""

        # Initialize members of the class
        self.name = name
        self.scope = scope
        self.plugin_bundle_id = plugin_bundle_id
        self.filter_browsers = filter_browsers
        self.filter_sockets = filter_sockets
        self.vendor_config = vendor_config


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
        scope = dictionary.get('scope')
        plugin_bundle_id = dictionary.get('PluginBundleID')
        filter_browsers = dictionary.get('FilterBrowsers')
        filter_sockets = dictionary.get('FilterSockets')
        vendor_config = None
        if dictionary.get('VendorConfig') != None:
            vendor_config = list()
            for structure in dictionary.get('VendorConfig'):
                vendor_config.append(meraki_sdk.models.vendor_config_model.VendorConfigModel.from_dictionary(structure))

        # Return an object of this model
        return cls(name,
                   scope,
                   plugin_bundle_id,
                   filter_browsers,
                   filter_sockets,
                   vendor_config)



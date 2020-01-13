# -*- coding: utf-8 -*-

"""
    meraki_sdk

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""

import meraki_sdk.models.provider_configuration_model

class AddNetworkSmProfileUmbrellaModel(object):

    """Implementation of the 'addNetworkSmProfileUmbrella' model.

    TODO: type model description here.

    Attributes:
        app_bundle_identifier (string): The bundle ID of the application,
            defaults to com.cisco.ciscosecurity.app
        provider_bundle_identifier (string): The bundle ID of the provider,
            defaults to com.cisco.ciscosecurity.app.CiscoUmbrella
        provider_configuration (list of ProviderConfigurationModel): The
            specific ProviderConfiguration to be passed to the filtering
            framework, in the form of an array of objects (as JSON).
        uses_cert (bool): Whether the certificate should be attached to this
            profile (one of true, false). False by default

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "provider_configuration":'ProviderConfiguration',
        "app_bundle_identifier":'AppBundleIdentifier',
        "provider_bundle_identifier":'ProviderBundleIdentifier',
        "uses_cert":'usesCert'
    }

    def __init__(self,
                 provider_configuration=None,
                 app_bundle_identifier=None,
                 provider_bundle_identifier=None,
                 uses_cert=None):
        """Constructor for the AddNetworkSmProfileUmbrellaModel class"""

        # Initialize members of the class
        self.app_bundle_identifier = app_bundle_identifier
        self.provider_bundle_identifier = provider_bundle_identifier
        self.provider_configuration = provider_configuration
        self.uses_cert = uses_cert


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
        provider_configuration = None
        if dictionary.get('ProviderConfiguration') != None:
            provider_configuration = list()
            for structure in dictionary.get('ProviderConfiguration'):
                provider_configuration.append(meraki_sdk.models.provider_configuration_model.ProviderConfigurationModel.from_dictionary(structure))
        app_bundle_identifier = dictionary.get('AppBundleIdentifier')
        provider_bundle_identifier = dictionary.get('ProviderBundleIdentifier')
        uses_cert = dictionary.get('usesCert')

        # Return an object of this model
        return cls(provider_configuration,
                   app_bundle_identifier,
                   provider_bundle_identifier,
                   uses_cert)



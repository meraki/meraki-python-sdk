# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""

import meraki.models.provider_configuration_model

class UpdateNetworkSmProfileUmbrellaModel(object):

    """Implementation of the 'updateNetworkSmProfileUmbrella' model.

    TODO: type model description here.

    Attributes:
        name (string): optional: A new name for the profile
        scope (string): optional: A new scope for the profile (one of all,
            none, withAny, withAll, withoutAny, or withoutAll) and a set of
            tags of the devices to be assigned
        app_bundle_identifier (string): optional: The bundle ID of the
            application
        provider_bundle_identifier (string): optional: The bundle ID of the
            provider
        provider_configuration (list of ProviderConfigurationModel): optional:
            The specific ProviderConfiguration to be passed to the filtering
            framework, in the form of an array of objects (as JSON).
        uses_cert (bool): optional: Whether the certificate should be attached
            to this profile (one of true, false)

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name":'name',
        "scope":'scope',
        "app_bundle_identifier":'AppBundleIdentifier',
        "provider_bundle_identifier":'ProviderBundleIdentifier',
        "provider_configuration":'ProviderConfiguration',
        "uses_cert":'usesCert'
    }

    def __init__(self,
                 name=None,
                 scope=None,
                 app_bundle_identifier=None,
                 provider_bundle_identifier=None,
                 provider_configuration=None,
                 uses_cert=None):
        """Constructor for the UpdateNetworkSmProfileUmbrellaModel class"""

        # Initialize members of the class
        self.name = name
        self.scope = scope
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
        name = dictionary.get('name')
        scope = dictionary.get('scope')
        app_bundle_identifier = dictionary.get('AppBundleIdentifier')
        provider_bundle_identifier = dictionary.get('ProviderBundleIdentifier')
        provider_configuration = None
        if dictionary.get('ProviderConfiguration') != None:
            provider_configuration = list()
            for structure in dictionary.get('ProviderConfiguration'):
                provider_configuration.append(meraki.models.provider_configuration_model.ProviderConfigurationModel.from_dictionary(structure))
        uses_cert = dictionary.get('usesCert')

        # Return an object of this model
        return cls(name,
                   scope,
                   app_bundle_identifier,
                   provider_bundle_identifier,
                   provider_configuration,
                   uses_cert)



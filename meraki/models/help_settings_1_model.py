# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class HelpSettings1Model(object):

    """Implementation of the 'HelpSettings1' model.

    Settings for describing the modifications to various Help page features.
    Each property in this object accepts one of
        'default or inherit' (do not modify functionality), 'hide' (remove the
        section from Dashboard), or 'show' (always show
        the section on Dashboard). Some properties in this object also accept
        custom HTML used to replace the section on
        Dashboard; see the documentation for each property to see the allowed
        values.

    Attributes:
        help_tab (HelpTabEnum): The Help tab, under which all support
            information resides. If this tab is hidden, no other 'Help'
            branding     customizations will be visible. Can be one of
            'default or inherit', 'hide' or 'show'.
        get_help_subtab (GetHelpSubtabEnum): The 'Help -> Get Help' subtab on
            which Cisco Meraki KB, Product Manuals, and Support/Case
            Information are displayed. Note     that if this subtab is hidden,
            branding customizations for the KB on 'Get help', Cisco Meraki
            product documentation,     and support contact info will not be
            visible. Can be one of 'default or inherit', 'hide' or 'show'.
        community_subtab (CommunitySubtabEnum): The 'Help -> Community' subtab
            which provides a link to Meraki Community. Can be one of 'default
            or inherit', 'hide' or 'show'.
        cases_subtab (CasesSubtabEnum): The 'Help -> Cases' Dashboard subtab
            on which Cisco Meraki support cases for this organization can be
            managed. Can be one     of 'default or inherit', 'hide' or
            'show'.
        data_protection_requests_subtab (DataProtectionRequestsSubtabEnum):
            The 'Help -> Data protection requests' Dashboard subtab on which
            requests to delete, restrict, or export end-user data can     be
            audited. Can be one of 'default or inherit', 'hide' or 'show'.
        get_help_subtab_knowledge_base_search (string): The KB search box
            which appears on the Help page. Can be one of 'default or
            inherit', 'hide', 'show', or a replacement custom HTML string.
        universal_search_knowledge_base_search
            (UniversalSearchKnowledgeBaseSearchEnum): The universal search box
            always visible on Dashboard will, by default, present results from
            the Meraki KB. This configures     whether these Meraki KB results
            should be returned. Can be one of 'default or inherit', 'hide' or
            'show'.
        cisco_meraki_product_documentation (string): The 'Product Manuals'
            section of the 'Help -> Get Help' subtab. Can be one of 'default
            or inherit', 'hide', 'show', or a replacement custom HTML string.
        support_contact_info (string): The 'Contact Meraki Support' section of
            the 'Help -> Get Help' subtab. Can be one of 'default or inherit',
            'hide', 'show', or a replacement custom HTML string.
        new_features_subtab (NewFeaturesSubtabEnum): The 'Help -> New
            features' subtab where new Dashboard features are detailed. Can be
            one of 'default or inherit', 'hide' or 'show'.
        firewall_info_subtab (FirewallInfoSubtabEnum): The 'Help -> Firewall
            info' subtab where necessary upstream firewall rules for
            communication to the Cisco Meraki cloud are     listed. Can be one
            of 'default or inherit', 'hide' or 'show'.
        api_docs_subtab (ApiDocsSubtabEnum): The 'Help -> API docs' subtab
            where a detailed description of the Dashboard API is listed. Can
            be one of     'default or inherit', 'hide' or 'show'.
        hardware_replacements_subtab (HardwareReplacementsSubtabEnum): The
            'Help -> Replacement info' subtab where important information
            regarding device replacements is detailed. Can be one of    
            'default or inherit', 'hide' or 'show'.
        sm_forums (SmForumsEnum): The 'SM Forums' subtab which links to
            community-based support for Cisco Meraki Systems Manager. Only
            configurable for     organizations that contain Systems Manager
            networks. Can be one of 'default or inherit', 'hide' or 'show'.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "help_tab":'helpTab',
        "get_help_subtab":'getHelpSubtab',
        "community_subtab":'communitySubtab',
        "cases_subtab":'casesSubtab',
        "data_protection_requests_subtab":'dataProtectionRequestsSubtab',
        "get_help_subtab_knowledge_base_search":'getHelpSubtabKnowledgeBaseSearch',
        "universal_search_knowledge_base_search":'universalSearchKnowledgeBaseSearch',
        "cisco_meraki_product_documentation":'ciscoMerakiProductDocumentation',
        "support_contact_info":'supportContactInfo',
        "new_features_subtab":'newFeaturesSubtab',
        "firewall_info_subtab":'firewallInfoSubtab',
        "api_docs_subtab":'apiDocsSubtab',
        "hardware_replacements_subtab":'hardwareReplacementsSubtab',
        "sm_forums":'smForums'
    }

    def __init__(self,
                 help_tab=None,
                 get_help_subtab=None,
                 community_subtab=None,
                 cases_subtab=None,
                 data_protection_requests_subtab=None,
                 get_help_subtab_knowledge_base_search=None,
                 universal_search_knowledge_base_search=None,
                 cisco_meraki_product_documentation=None,
                 support_contact_info=None,
                 new_features_subtab=None,
                 firewall_info_subtab=None,
                 api_docs_subtab=None,
                 hardware_replacements_subtab=None,
                 sm_forums=None):
        """Constructor for the HelpSettings1Model class"""

        # Initialize members of the class
        self.help_tab = help_tab
        self.get_help_subtab = get_help_subtab
        self.community_subtab = community_subtab
        self.cases_subtab = cases_subtab
        self.data_protection_requests_subtab = data_protection_requests_subtab
        self.get_help_subtab_knowledge_base_search = get_help_subtab_knowledge_base_search
        self.universal_search_knowledge_base_search = universal_search_knowledge_base_search
        self.cisco_meraki_product_documentation = cisco_meraki_product_documentation
        self.support_contact_info = support_contact_info
        self.new_features_subtab = new_features_subtab
        self.firewall_info_subtab = firewall_info_subtab
        self.api_docs_subtab = api_docs_subtab
        self.hardware_replacements_subtab = hardware_replacements_subtab
        self.sm_forums = sm_forums


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
        help_tab = dictionary.get('helpTab')
        get_help_subtab = dictionary.get('getHelpSubtab')
        community_subtab = dictionary.get('communitySubtab')
        cases_subtab = dictionary.get('casesSubtab')
        data_protection_requests_subtab = dictionary.get('dataProtectionRequestsSubtab')
        get_help_subtab_knowledge_base_search = dictionary.get('getHelpSubtabKnowledgeBaseSearch')
        universal_search_knowledge_base_search = dictionary.get('universalSearchKnowledgeBaseSearch')
        cisco_meraki_product_documentation = dictionary.get('ciscoMerakiProductDocumentation')
        support_contact_info = dictionary.get('supportContactInfo')
        new_features_subtab = dictionary.get('newFeaturesSubtab')
        firewall_info_subtab = dictionary.get('firewallInfoSubtab')
        api_docs_subtab = dictionary.get('apiDocsSubtab')
        hardware_replacements_subtab = dictionary.get('hardwareReplacementsSubtab')
        sm_forums = dictionary.get('smForums')

        # Return an object of this model
        return cls(help_tab,
                   get_help_subtab,
                   community_subtab,
                   cases_subtab,
                   data_protection_requests_subtab,
                   get_help_subtab_knowledge_base_search,
                   universal_search_knowledge_base_search,
                   cisco_meraki_product_documentation,
                   support_contact_info,
                   new_features_subtab,
                   firewall_info_subtab,
                   api_docs_subtab,
                   hardware_replacements_subtab,
                   sm_forums)



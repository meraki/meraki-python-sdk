# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class WhitelistedRuleModel(object):

    """Implementation of the 'WhitelistedRule' model.

    TODO: type model description here.

    Attributes:
        rule_id (string): A rule identifier of the format
            meraki:intrusion/snort/GID/<gid>/SID/<sid>. gid and sid can be
            obtained from either https://www.snort.org/rule-docs or as ruleIds
            from the security events in /organization/[orgId]/securityEvents
        message (string): Message is optional and is ignored on a PUT call. It
            is allowed in order for PUT to be compatible with GET

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "rule_id":'ruleId',
        "message":'message'
    }

    def __init__(self,
                 rule_id=None,
                 message=None):
        """Constructor for the WhitelistedRuleModel class"""

        # Initialize members of the class
        self.rule_id = rule_id
        self.message = message


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
        rule_id = dictionary.get('ruleId')
        message = dictionary.get('message')

        # Return an object of this model
        return cls(rule_id,
                   message)



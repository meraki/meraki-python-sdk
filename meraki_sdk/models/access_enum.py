# -*- coding: utf-8 -*-

"""
    meraki_sdk

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""

class AccessEnum(object):

    """Implementation of the 'Access' enum.

    A string indicating the rule for which IPs are allowed to use the
    specified service. Acceptable values are "blocked" (no remote IPs can
    access the service), "restricted" (only whitelisted IPs can access the
    service), and "unrestriced" (any remote IP can access the service). This
    field is required

    Attributes:
        BLOCKED: TODO: type description here.
        RESTRICTED: TODO: type description here.
        UNRESTRICTED: TODO: type description here.

    """

    BLOCKED = 'blocked'

    RESTRICTED = 'restricted'

    UNRESTRICTED = 'unrestricted'


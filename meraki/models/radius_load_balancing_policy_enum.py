# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""

class RadiusLoadBalancingPolicyEnum(object):

    """Implementation of the 'RadiusLoadBalancingPolicy' enum.

    This policy determines which RADIUS server will be contacted first in an
    authentication attempt and the ordering of any necessary retry attempts
    ('Strict priority order' or 'Round robin')

    Attributes:
        ENUM_STRICT PRIORITY ORDER: TODO: type description here.
        ENUM_ROUND ROBIN: TODO: type description here.

    """

    ENUM_STRICT_PRIORITY_ORDER = 'Strict priority order'

    ENUM_ROUND_ROBIN = 'Round robin'


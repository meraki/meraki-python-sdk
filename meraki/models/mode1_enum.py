# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""

class Mode1Enum(object):

    """Implementation of the 'Mode1' enum.

    Either 'renew' or 'addDevices'. 'addDevices' will increase the license
    limit, while 'renew' will extend the amount of time until expiration.
    Please see <a target='_blank'
    href='https://documentation.meraki.com/zGeneral_Administration/Licensing/Ad
    ding_an_Enterprise_license_to_an_existing_Dashboard_account'>this
    article</a> for more information.

    Attributes:
        ADDDEVICES: TODO: type description here.
        RENEW: TODO: type description here.

    """

    ADDDEVICES = 'addDevices'

    RENEW = 'renew'

